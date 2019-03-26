
from src.common import standard

from src.model.photo import Photo


def find(id):

    photo = Photo.find(id)

    return standard.response(response=photo, message=f'Successfully retrieved photo: {id}')
