import json
import boto3
from django.conf import settings

import frontmatter
from minio.error import S3Error
from app.models import Test, Course
from app.services.minio_client import list_items_in_bucket, minio_client

AWS_S3_ENDPOINT_URL = settings.AWS_S3_ENDPOINT_URL
AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY

s3 = boto3.client(
    "s3",
    endpoint_url=AWS_S3_ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


def set_folder_public(
    is_public: bool,
    bucket_name: str,
    directory: str = "tests",
):
    if is_public:
        policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": f"arn:aws:s3:::{bucket_name}/{directory}/*",
                }
            ],
        }
    else:
        policy = {"Version": "2012-10-17", "Statement": []}

    s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(policy))


def sync_tests():
    courses = set(Course.objects.values_list("name", flat=True))
    created_tests = 0

    for course_name in courses:
        test_names = list_items_in_bucket(course_name, "tests/")

        course = Course.objects.get(name=course_name)
        existing_tests = set(
            Test.objects.filter(course=course).values_list("name", flat=True)
        )
        new_tests = set(test_names) - existing_tests
        tests_to_create = [
            Test(
                name=test_name[:-3],
                title=f"{get_test_title_from_metadata(course_name, test_name)}",
                course=course,
                content_url=f"{course_name}/tests/{test_name}",
            )
            for i, test_name in enumerate(new_tests)
        ]
        Test.objects.bulk_create(tests_to_create)
        created_tests += len(tests_to_create)

    return created_tests


def get_test_title_from_metadata(course_name: str, test_name: str) -> str:
    bucket_name = course_name
    file_path = f"tests/{test_name}"

    try:
        obj = minio_client.get_object(bucket_name, file_path)

        file_content = obj.read().decode("utf-8")

        test_metadata = frontmatter.loads(file_content)

        title = test_metadata.get("title", f"Рубежный контроль")

        return title

    except S3Error as e:
        print(f"Ошибка при получении файла {file_path} из MinIO: {e}")
        return ""
