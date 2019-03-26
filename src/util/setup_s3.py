
from src.aws.s3 import get_s3
from src.common.config import Config
from src.common import constants


if __name__ == '__main__':

    Config.setup()
    s3 = get_s3('local')

    s3.create_bucket(Bucket=constants.S3_BUCKET_NAME, CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})

    print('############')
    print('S3 Ready')
    print('############')
