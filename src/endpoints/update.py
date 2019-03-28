"""update is the module that handles updating
photo and metadata data via the update PUT
endpoint"""

from flask import request

from src.common import standard
from src.model.photo import Photo
from src.aws.s3_service import S3Service


def update(photo_id):

    patch = {}

    photo_file = request.files.get('photo', None)
    if photo_file is not None:
        s3_url, s3_thumbnail_url = S3Service.upload_file(photo_file)
        patch['photo_url'] = s3_url
        patch['thumbnail_url'] = s3_thumbnail_url
        patch['filename'] = photo_file.filename

    description = request.form.get('description', None)
    if description is not None:
        patch['description'] = description

    title = request.form.get('title', None)
    if title is not None:
        patch['title'] = title

    photo = Photo.find(photo_id).patch(patch)

    return standard.response(body=photo, message="Successfully updated photo")
