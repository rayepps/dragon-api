"""s3_service manages uploading and fetching files from s3"""

from werkzeug.utils import secure_filename

from src.common import constants
from src.common import exceptions
from src.aws import client as aws


class S3Service:

    @classmethod
    def generate_url(cls, s3, filename):
        return f'{s3.meta.endpoint_url}/{constants.S3_BUCKET_NAME}/{filename}'

    @classmethod
    def upload_file(cls, file):
        """uploads a file to s3 without saving it locally

        @param file: werkzeug.datastructures.FileStorage

        @return str: A string with the full s3 path to the file
        """

        if not cls.validate_file_type(file.filename):
            raise exceptions.invalid_file_type.add(file.filename)

        filename = secure_filename(file.filename)

        s3 = aws.s3()
        s3.put_object(Body=file.read(), Bucket=constants.S3_BUCKET_NAME, Key=filename)

        full_size_photo_url = cls.generate_url(s3, filename)
        thumbnail_photo_url = full_size_photo_url

        return full_size_photo_url, thumbnail_photo_url

    @classmethod
    def remove_file(cls, filename):
        aws.s3().Object(constants.S3_BUCKET_NAME, filename).delete()

    @classmethod
    def validate_file_type(cls, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in constants.FILE_TYPE_WHITELIST
