"""ssm service module manages fetching keys from ssm service"""

from dragon.aws import client as aws


def get(name):
    ssm_response = aws.ssm().get_parameter(Name=name, WithDecryption=True)

    return ssm_response.get('Parameter').get('Value')
