"""upload is the module that handles file
uploads via the upload POST endpoint"""

from flask import request

from src.common import standard
from src.common import exceptions
from src.model.photo import Photo
from src.aws.services import s3


def upload():

    photo_file = request.files.get('photo', None)
    title = request.form.get('title', None)
    description = request.form.get('description', None)

    if photo_file is None:
        raise exceptions.missing_parameter.add('photo')

    if title is None:
        raise exceptions.missing_parameter.add('title')

    if description is None:
        raise exceptions.missing_parameter.add('description')

    Photo.validate_file_type(photo_file.filename)

    s3.upload(photo_file.read(), photo_file.filename)
    s3_url = s3.generate_url(photo_file.filename)

    photo = Photo(dict(
        title=title,
        filename=photo_file.filename,
        description=description,
        photo_url=s3_url,
        thumbnail_url=s3_url
    ))

    photo.save()

    return standard.response(body=photo, message="Successfully uploaded photo")
