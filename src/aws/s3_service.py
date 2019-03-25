
import boto3
from werkzeug.utils import secure_filename

from src.common.config import Config


class S3Service:

    @classmethod
    def upload_file(cls, file):
        """uploads a file to s3 without saving it locally

        @param file: werkzeug.datastructures.FileStorage

        @return str: A string with the full s3 path to the file
        """

        filename = secure_filename(file.filename)

        client = boto3.client('s3')

        client.put_object(Body=file.read(), Bucket=Config.s3_bucket_name, Key=filename)

        return f'{Config.s3_bucket_name}/{filename}'
