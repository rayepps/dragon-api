
from os import environ as env


class Config:

    version = 'unknown'
    upload_folder = '/tmp'
    s3_bucket_name = 'dragon-photo-storage'
    dynamo_host = env.get('DYNAMO_HOST')
    dynamo_port = env.get('DYNAMO_PORT')
    exec_env = env.get('EXEC_ENV')

    @classmethod
    def setup(cls):
        with open('/usr/src/dragon-api/version.cfg') as f:
            cls.version = f.read().replace('\n', '')
