"""s3_service manages uploading and fetching files from s3"""

from dragon.common import constants
from dragon.aws import client as aws


def upload(data, filename):
    aws.s3().Object(constants.S3_BUCKET_NAME, filename).put(Body=data)


def generate_url(filename):
    return f'{aws.s3().meta.client.meta.endpoint_url}/{constants.S3_BUCKET_NAME}/{filename}'


def remove(filename):
    aws.s3().Object(constants.S3_BUCKET_NAME, filename).delete()
