from app.models import UsefulPost
from app.services.minio_client import list_items_in_bucket, minio_client
from django.conf import settings
from datetime import datetime
import frontmatter


def sync_useful():

    useful = list_items_in_bucket("useful")
    print(useful)

    posts_to_create = []
    for useful_name in useful:
        metadata = get_useful_metadata(useful_name)
        post = UsefulPost(
            name=useful_name,
            title=metadata["title"],
            content_url=f"{settings.AWS_S3_ENDPOINT_URL}/useful/{useful_name}",
            description=metadata["description"],
            semester=metadata["semester"],
            lastUpdate=datetime.now(),
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
