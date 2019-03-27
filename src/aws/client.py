
import boto3

from src.common.config import Config


def s3():
    if Config.exec_env == 'local':
        return boto3.client('s3', endpoint_url=Config.s3_url)
    else:
        return boto3.client('s3')

def ssm():
    if Config.exec_env == 'local':
        return boto3.client('ssm', endpoint_url=Config.ssm_url)
    else:
        return boto3.client('ssm')

def dynamo():
    if Config.exec_env == 'local':
        return boto3.resource('dynamodb', endpoint_url=Config.dynamo_url)
    else:
        return boto3.resource('dynamodb')
