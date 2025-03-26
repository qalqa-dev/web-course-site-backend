import json
import boto3
from django.conf import settings


AWS_S3_ENDPOINT_URL = settings.AWS_S3_ENDPOINT_URL
AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY

s3 = boto3.client(
    "s3",
    endpoint_url=AWS_S3_ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


def set_folder_public(
    is_public: bool,
    bucket_name: str,
    directory: str = "tests",
):
    if is_public:
        policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": f"arn:aws:s3:::{bucket_name}/{directory}/*",
                }
            ],
        }
    else:
        policy = {"Version": "2012-10-17", "Statement": []}

    s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(policy))
