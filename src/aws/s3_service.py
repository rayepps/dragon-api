
import boto3
from werkzeug.utils import secure_filename

from src.common.config import Config
from src.common import validation


class S3Service:

    @classmethod
    def upload_file(cls, file):
        """uploads a file to s3 without saving it locally

        @param file: werkzeug.datastructures.FileStorage

        @return str: A string with the full s3 path to the file
        """

        if not validation.validate_file_type(file.filename):
            raise exceptions.invalid_file_type(file.filename)

        filename = secure_filename(file.filename)

        s3 = boto3.client('s3')

        s3.put_object(Body=file.read(), Bucket=Config.s3_bucket_name, Key=filename)

        return f'{s3.meta.endpoint_url}/{Config.s3_bucket_name}/{filename}'

    @classmethod
    def remove_file(cls, filename):
        s3 = boto3.resource('s3')
        s3.Object(Config.s3_bucket_name, filename).delete()
