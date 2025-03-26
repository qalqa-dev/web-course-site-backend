from django.core.management.base import BaseCommand
from app.services.tests_service import sync_tests


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.stdout.write(
            self.style.NOTICE("Идет синхронизация рубежных контрольных...")
        )
        count = sync_tests()
        self.stdout.write(
            self.style.SUCCESS(f"Добавлено {count} новых рубежных контрольных")
        )
