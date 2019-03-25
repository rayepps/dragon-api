
from src.common import standard
from src.aws.s3_service import S3Service

from src.dal.model.photo import Photo


def remove(id):

    photo = Photo(dict(photo_id=id))

    S3Service.remove_file(photo.obj['filename'])

    photo.delete()

    return standard.response(message=f'Successfully deleted photo: {id}')
