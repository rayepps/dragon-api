

import boto3

from src.common.config import Config


def get_dynamo(env):
    if env == 'local':
        return boto3.resource('dynamodb', endpoint_url=Config.dynamo_url)
    else:
        return boto3.resource('dynamodb')
