
from flask import request

from src.common.config import Config
from src.common import standard

from src.dal.model.photo import Photo

from src.aws.s3_service import S3Service


def update(id):

    photo = Photo(dict(photo_id=id))

    title = request.form.get('title', None)
    if title is not None:
        photo.obj['title'] = title

    description = request.form.get('description', None)
    if description is not None:
        photo.obj['description'] = description

    photo_file = request.files.get('photo', None)
    if photo_file is not None:
        photo.obj['photo_url'] = S3Service.upload_file(photo_file)
        photo.obj['filename'] = photo_file.filename

    photo.save()

    return standard.response(response=photo, message="Successfully updated photo")
