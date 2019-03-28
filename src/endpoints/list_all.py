"""list_all module handles GET request
from client and does the work of fetching
all photo metadata from the database"""


from src.common import standard
from src.model.photo import Photo


def list_all():

    photos = Photo.get_all()

    return standard.response(body=photos, message="Successfully retrieved photo list")
