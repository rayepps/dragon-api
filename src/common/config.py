
from os import environ as env


class Config:

    version = 'unknown'
    dynamo_url = env.get('DYNAMO_URL')
    s3_url = env.get('S3_URL')
    exec_env = env.get('EXEC_ENV')
    api_key = env.get('API_KEY')
    ssm_url = env.get('SSM_URL')

    @classmethod
    def setup(cls):
        with open('/usr/src/dragon-api/version.cfg') as f:
            cls.version = f.read().replace('\n', '')
