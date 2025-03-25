from django.core.management.base import BaseCommand
from app.services.useful_service import sync_useful


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write(
            self.style.WARNING(
                "Идет синхронизация статей... (Может занять некоторое время)"
            )
        )
        count = sync_useful()
        self.stdout.write(self.style.SUCCESS(f"Добавлено {count} новых cтатей"))
