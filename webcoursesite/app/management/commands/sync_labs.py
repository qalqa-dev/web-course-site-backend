from django.core.management.base import BaseCommand
from app.services.lab_service import sync_labs


class Command(BaseCommand):
    help = "Синхронизирует лабораторные работы из MinIO в базу данных"

    def handle(self, *args, **kwargs):
        count = sync_labs()
        self.stdout.write(
            self.style.SUCCESS(f"Добавлено {count} новых лабораторных работ")
        )
