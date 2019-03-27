
from src.aws import client as aws
from src.common.config import Config
from src.common import constants


if __name__ == '__main__':

    Config.setup()

    aws.s3().create_bucket(Bucket=constants.S3_BUCKET_NAME, CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})

    print('############')
    print('S3 Ready')
    print('############')
