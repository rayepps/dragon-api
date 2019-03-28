"""remove module handles DELETE requests
from the client and does the work of
finding the specified photo and deleting
it from the database and file storage service"""

from src.common import standard
from src.aws.s3_service import S3Service

from src.model.photo import Photo


def remove(photo_id):

    photo = Photo.find(photo_id)

    S3Service.remove_file(photo.store['filename'])

    photo.delete()

    return standard.response(body=f'Successfully deleted photo: {id}')
