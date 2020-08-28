"""aws client module is a one stop shop to get
boto3 client objects already assigned to the
correct resource url"""

import boto3

from dragon.common.config import Config


def s3():
    if Config.exec_env == 'local':
        return boto3.resource('s3', endpoint_url=Config.s3_url)
    return boto3.resource('s3')

def ssm():
    if Config.exec_env == 'local':
        return boto3.client('ssm', endpoint_url=Config.ssm_url)
    return boto3.client('ssm', region_name='us-west-2')

def dynamo():
    if Config.exec_env == 'local':
        return boto3.resource('dynamodb', endpoint_url=Config.dynamo_url)
    return boto3.resource('dynamodb')
