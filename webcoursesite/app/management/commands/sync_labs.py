from django.core.management.base import BaseCommand
from app.services.lab_service import sync_labs


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE("Идет синхронизация лабораторных работ..."))
        count = sync_labs()
        self.stdout.write(
            self.style.SUCCESS(f"Добавлено {count} новых лабораторных работ")
        )
