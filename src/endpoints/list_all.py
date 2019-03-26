
from src.common import standard

from src.model.photo import Photo


def list_all():

    photos = Photo.get_all()

    return standard.response(response=photos, message="Successfully retrieved photo list")
