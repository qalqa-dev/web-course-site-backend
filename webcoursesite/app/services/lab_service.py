from app.models import Lab, Course
from app.services.minio_client import list_items_in_bucket, minio_client
from django.conf import settings
from minio.error import S3Error
import re
import frontmatter


def sync_labs():
    course_names = set(Course.objects.values_list("name", flat=True))
    created_labs = 0

    for course_name in course_names:
        lab_names = list_items_in_bucket(course_name, "labs/")

        course = Course.objects.get(name=course_name)
        existing_labs = set(
            Lab.objects.filter(course=course).values_list("name", flat=True)
        )
        new_labs = set(lab_names) - existing_labs
        labs_to_create = [
            Lab(
                name=lab_name,
                title=f"{get_lab_title_from_metadata(course_name, lab_name)}",
                number=extract_lab_number(lab_name),
                course=course,
                content_url=f"{settings.AWS_S3_ENDPOINT_URL}/{course_name}/labs/{lab_name}",
            )
            for i, lab_name in enumerate(new_labs)
        ]
        Lab.objects.bulk_create(labs_to_create)
        created_labs += len(labs_to_create)

    return created_labs


def extract_lab_number(file_name: str) -> int:
    if file_name == "intro.md":
        return 0

    match = re.match(r"laba(\d+)\.md", file_name)
    if match:
        return int(match.group(1))

    return -1


def get_lab_title_from_metadata(course_name: str, lab_name: str) -> str:
    bucket_name = course_name
    file_path = f"labs/{lab_name}"

    try:
        obj = minio_client.get_object(bucket_name, file_path)

        file_content = obj.read().decode("utf-8")

        lab_metadata = frontmatter.loads(file_content)

        title = lab_metadata.get(
            "title", f"Лабораторная работа {extract_lab_number(lab_name)}"
        )

        return title

    except S3Error as e:
        print(f"Ошибка при получении файла {file_path} из MinIO: {e}")
        return ""
