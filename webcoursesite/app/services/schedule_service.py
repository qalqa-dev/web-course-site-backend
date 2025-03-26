from app.models import Course, Schedule
from app.services.minio_client import (
    check_if_file_exists_in_course_bucket,
    get_s3_file_url,
)


def sync_schedule():
    courses = Course.objects.all()

    for course in courses:
        file_exists = check_if_file_exists_in_course_bucket(course.name, "plan.md")

        if file_exists:
            file_url = get_s3_file_url(course.name, "plan.md")

            if not hasattr(course, "schedule"):
                schedule = Schedule(
                    course=course,
                    name="plan.md",
                    title="План курса",
                    content_url=file_url,
                )
                schedule.save()
                print(f"Добавлено расписание для курса {course.name}")
            else:
                print(f"Расписание для курса {course.name} уже существует.")
        else:
            print(f"Файл расписания не найден для курса {course.name}.")
