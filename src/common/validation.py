
from src.common import constants


def validate_file_type(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in constants.FILE_TYPE_WHITELIST
