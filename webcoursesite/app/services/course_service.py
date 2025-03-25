from app.models import Course
from app.services.minio_client import list_buckets
from datetime import datetime
from app.services.lab_service import sync_labs
from app.services.schedule_service import sync_schedule

DEFAULT_EXCLUDED_BUCKETS = {"photos", "useful"}


def sync_courses(excluded_buckets=None):
    if excluded_buckets is None:
        excluded_buckets = []

    all_buckets = set(list_buckets())

    excluded_buckets = set(excluded_buckets) | DEFAULT_EXCLUDED_BUCKETS
    valid_buckets = all_buckets - excluded_buckets

    existing_courses = set(Course.objects.values_list("name", flat=True))

    new_courses = valid_buckets - existing_courses

    courses_to_create = [
        Course(
            name=course_name,
            title=course_name,
            description="",
            statement="",
            year=datetime.now().year,
        )
        for course_name in new_courses
    ]
    Course.objects.bulk_create(courses_to_create)

    sync_labs()
    sync_schedule()

    return len(courses_to_create)
