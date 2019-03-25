
from http import HTTPStatus

from src.common import standard
from src.common import codes
from src.common import exceptions


def catch_errors(handler):

    def middle(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except exceptions.DragonException as ex:
            # TODO: Log error message
            print(ex)
            return standard.error(http_status=ex.http_status, code=ex.code, message=ex.message)
        except Exception as ex:
            # TODO: Log error message
            print(ex)
            return standard.error(http_status=HTTPStatus.INTERNAL_SERVER_ERROR, code=codes.UNKNOWN_ERROR, message="Unknown error occurred")

    return middle
