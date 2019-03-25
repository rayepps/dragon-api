
from flask import request

from src.common.config import Config
from src.common import standard
from src.common import exceptions

from src.dal.model.photo import Photo

from src.aws.s3_service import S3Service


def upload():

    photo_file = request.files.get('photo', None)

    if photo_file is None:
        raise exceptions.missing_parameter('photo')

    s3_url = S3Service.upload_file(photo_file)

    photo = Photo(dict(
        title=request.form.get('title', ''),
        filename=photo_file.filename,
        description=request.form.get('description', ''),
        photo_url=s3_url
    ))

    photo.save()

    return standard.response(response=photo, message="Successfully uploaded photo")
