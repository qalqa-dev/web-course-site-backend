import argparse
from django.core.management.base import BaseCommand
from app.services.tests_service import set_folder_public


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "access",
            choices=["public", "private"],
        )
        parser.add_argument("bucket")
        parser.add_argument("--folder", default="tests")

    def handle(self, *args, **options):
        access = options["access"]
        bucket_name = options["bucket"]
        directory = options["folder"]

        is_public = access == "public"
        set_folder_public(is_public, bucket_name, directory)
        status = "публичная" if is_public else "приватная"
        self.stdout.write(f"Директория '{directory}' теперь {status}.")
