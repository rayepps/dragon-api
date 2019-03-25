import os

from flask import request
from werkzeug.utils import secure_filename

from src.common.config import Config
from src.common import standard
from src.common import validation
from src.common import exceptions

from src.aws.s3_service import S3Service


def upload():

    if 'photo' not in request.files:
        raise exceptions.missing_parameter('photo')

    photo = request.files['photo']

    if not validation.validate_file_type(photo.filename):
        raise exceptions.invalid_file_type(photo.filename)

    S3Service.upload_file(photo)

    # TODO: add to dynamo

    return standard.response(message="Successfully uploaded photo")
