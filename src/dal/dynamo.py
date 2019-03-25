

import boto3

from src.common.config import Config


def get_dynamo(env):
    if env == 'local':
        dynamo_url = f'{Config.dynamo_host}:{Config.dynamo_port}'
        print(f'### DYNAMO: {dynamo_url}')
        return boto3.resource('dynamodb', endpoint_url=dynamo_url)
    else:
        return boto3.resource('dynamodb')
