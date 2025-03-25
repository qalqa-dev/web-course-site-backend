from django.core.management.base import BaseCommand
from app.services.course_service import sync_courses


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            "--exclude",
            nargs="+",
            type=str,
            default=[],
        )

    def handle(self, *args, **options):
        excluded_buckets = options["exclude"]
        created_count = sync_courses(excluded_buckets)
        self.stdout.write(self.style.SUCCESS(f"Добавлено {created_count} новых курсов"))
