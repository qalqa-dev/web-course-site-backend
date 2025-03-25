from django.core.management.base import BaseCommand
from app.services.schedule_service import sync_schedule


class Command(BaseCommand):
    help = "Синхронизирует расписание курсов из MinIO"

    def handle(self, *args, **kwargs):
        sync_schedule()
