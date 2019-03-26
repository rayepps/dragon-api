
import boto3

from src.common.config import Config


def get_s3(env):
    if env == 'local':
        return boto3.client('s3', endpoint_url=Config.s3_url)
    else:
        return boto3.client('s3')
