from minio import Minio
from django.conf import settings

minio_client = Minio(
    settings.AWS_S3_ENDPOINT_URL.replace("http://", "").replace("https://", ""),
    access_key=settings.AWS_ACCESS_KEY_ID,
    secret_key=settings.AWS_SECRET_ACCESS_KEY,
    secure=False,
)


def list_buckets():
    """Получает список всех бакетов (курсов) в MinIO"""
    return [bucket.name for bucket in minio_client.list_buckets()]


def list_labs_in_course(course_name: str):
    prefix = "labs/"
    objects = minio_client.list_objects(course_name, prefix=prefix, recursive=True)

    lab_names = set()
    for obj in objects:
        parts = obj.object_name[len(prefix) :].split("/")
        if parts[0]:
            lab_names.add(parts[0])

    return list(lab_names)


def check_if_file_exists_in_course_bucket(course_name: str, filename: str) -> bool:
    try:
        prefix = filename
        objects = minio_client.list_objects(
            course_name, prefix=filename, recursive=False
        )
        return any(obj.object_name == prefix for obj in objects)
    except Exception as e:
        print(f"Ошибка при проверке файла в MinIO: {e}")
        return False


def get_s3_file_url(course_name: str, filename: str) -> str:
    return f"{settings.AWS_S3_ENDPOINT_URL}/{course_name}/{filename}"
