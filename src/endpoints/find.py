"""find module handles GET requests from
the client and does the work of finding
the specified photo and returning its
metadata"""

from src.common import standard

from src.model.photo import Photo


def find(photo_id):

    photo = Photo.find(photo_id)

    return standard.response(body=photo, message=f'Successfully retrieved photo: {photo_id}')
