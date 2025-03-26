from app.models import UsefulPost
from app.services.minio_client import list_items_in_bucket, minio_client
from django.conf import settings
from datetime import datetime
from minio.error import S3Error
import frontmatter
import requests
import os
from dotenv import load_dotenv
import sys
from tqdm import tqdm


def clear_console():
    os.system("cls" if sys.platform == "win32" else "clear")


def sync_useful():
    clear_console()
    useful = list_items_in_bucket("useful")

    existing_posts = set(UsefulPost.objects.values_list("name", flat=True))
    new_posts = set(useful) - existing_posts
    posts_to_create = []

    for useful_name in tqdm(
        new_posts, desc="Syncing useful posts", unit="post", colour="blue"
    ):
        metadata = get_useful_metadata(useful_name)

        post = UsefulPost(
            name=useful_name,
            title=metadata["title"],
            content_url=f"{settings.AWS_S3_ENDPOINT_URL}/useful/{useful_name}",
            description=metadata["description"],
            semester=metadata["semester"],
            lastUpdate=get_last_edit_date(useful_name),
            date=metadata["date"],
        )
        posts_to_create.append(post)

    UsefulPost.objects.bulk_create(posts_to_create)

    return len(posts_to_create)


def get_useful_metadata(post_name: str) -> dict:
    try:
        obj = minio_client.get_object("useful", post_name)
        file_content = obj.read().decode("utf-8")
        metadata = frontmatter.loads(file_content)

        return {
            "title": metadata.get("title", ""),
            "date": metadata.get("date", datetime.now()),
            "semester": metadata.get("semester", 1),
            "description": metadata.get("description", ""),
        }

    except S3Error as e:
        print(f"Error getting file {post_name} from MinIO: {e}")
        return {"title": "", "date": datetime.now(), "semester": 1}


load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def get_last_edit_date(filename: str) -> str:
    try:
        headers = {
            "Authorization": f"Bearer {GITHUB_TOKEN}",
        }
        response = requests.get(
            f"https://api.github.com/repos/slavaver/web-course-site/commits",
            params={"path": f"/src/useful/{filename}", "per_page": 1},
            headers=headers,
        )
        response.raise_for_status()
        commits = response.json()

        if not commits:
            return None

        commit_date = datetime.fromisoformat(
            commits[0]["commit"]["author"]["date"].replace("Z", "+00:00")
        )
        return commit_date.strftime("%Y-%m-%d")

    except (requests.RequestException, KeyError, ValueError):
        return None
