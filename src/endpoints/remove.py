"""remove module handles DELETE requests
from the client and does the work of
finding the specified photo and deleting
it from the database and file storage service"""

from src.common import standard
from src.aws.services import s3

from src.model.photo import Photo


def remove(photo_id):

    photo = Photo.find(photo_id)

    s3.remove(photo.store['filename'])

    photo.delete()

    return standard.response(body=f'Successfully deleted photo: {photo_id}')
