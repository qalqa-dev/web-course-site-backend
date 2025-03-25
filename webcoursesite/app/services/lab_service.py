from app.models import Lab, Course
from app.services.minio_client import list_labs_in_course
from django.conf import settings


def sync_labs():
    """Синхронизирует лабораторные работы из MinIO с базой данных"""
    course_names = set(Course.objects.values_list("name", flat=True))
    created_labs = 0

    for course_name in course_names:
        lab_names = list_labs_in_course(course_name)

        course = Course.objects.get(name=course_name)
        existing_labs = set(
            Lab.objects.filter(course=course).values_list("title", flat=True)
        )
        new_labs = set(lab_names) - existing_labs
        labs_to_create = [
            Lab(
                title=lab_name,
                number=i + 1,
                course=course,
                content_url=f"{settings.AWS_S3_ENDPOINT_URL}/{course_name}/labs/{lab_name}",
            )
            for i, lab_name in enumerate(new_labs)
        ]
        Lab.objects.bulk_create(labs_to_create)
        created_labs += len(labs_to_create)

    return created_labs
