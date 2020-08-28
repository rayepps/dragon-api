# pylint: disable=invalid-name
"""exceptions contains our custom exceptions"""

from http import HTTPStatus

from dragon.common import codes


class DragonException(Exception):

    def __init__(self, http_status, code, message):
        super().__init__(message)
        self.http_status = http_status
        self.code = code
        self.message = message

    def add(self, message):
        """add is a chainable method that concatenates the provided
        message onto the instances message attribute to provide more
        information"""
        self.message = f'{self.message}; {message}'
        return self


missing_parameter = DragonException(
    http_status=HTTPStatus.BAD_REQUEST,
    code=codes.MISSING_PARAMETER_ERROR,
    message='Missing a required parameter')

missing_header = DragonException(
    http_status=HTTPStatus.BAD_REQUEST,
    code=codes.MISSING_HEADER_ERROR,
    message='Missing a required header')

invalid_file_type = DragonException(
    http_status=HTTPStatus.BAD_REQUEST,
    code=codes.INVALID_FILE_TYPE,
    message='Invalid file type')

unauthorized = DragonException(
    http_status=HTTPStatus.UNAUTHORIZED,
    code=codes.INVALID_API_KEY,
    message='Invalid api key')

entity_not_found = DragonException(
    http_status=HTTPStatus.BAD_REQUEST,
    code=codes.TODO_NOT_FOUND,
    message='The todo id could not be found')
