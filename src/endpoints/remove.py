
from src.common import standard
from src.aws.s3_service import S3Service

from src.model.photo import Photo


def remove(id):

    photo = Photo.find(id)

    S3Service.remove_file(photo.store['filename'])

    photo.delete()

    return standard.response(message=f'Successfully deleted photo: {id}')
