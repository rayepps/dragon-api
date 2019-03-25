
from http import HTTPStatus

from src.common import codes
from src.common import constants


class DragonException(Exception):

    def __init__(self, http_status, code, message):
        self.http_status = http_status
        self.code = code
        self.message = message



missing_parameter = lambda parameter: DragonException(HTTPStatus.BAD_REQUEST, codes.MISSING_PARAMETER_ERROR, f'Missing a required parameter: {parameter}')
invalid_file_type = lambda file_type: DragonException(HTTPStatus.BAD_REQUEST, codes.INVALID_FILE_TYPE, f'Invalid file type: {file_type}. Only {constants.FILE_TYPE_WHITELIST}')
