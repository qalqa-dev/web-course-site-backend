from django.core.management.base import BaseCommand
from app.services.useful_service import sync_useful


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        sync_useful()
