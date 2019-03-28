"""middleware module that manages all exceptions that
occur during the execution of an endpoint handler"""

import sys
import traceback
from functools import wraps

from http import HTTPStatus

from src.common import standard
from src.common import codes
from src.common import exceptions


def catch_errors(handler):

    @wraps(handler)
    def middle(*args, **kwargs):
        # pylint: disable=broad-except
        try:
            return handler(*args, **kwargs)
        except exceptions.DragonException as ex:
            # TODO: Log error message
            print(ex)
            return standard.error(
                http_status=ex.http_status,
                code=ex.code,
                message=ex.message)
        except Exception as ex:
            # TODO: Log error message
            type_, value, tb = sys.exc_info()
            print(type_)
            print(value)
            traceback.print_tb(tb)
            return standard.error(
                http_status=HTTPStatus.INTERNAL_SERVER_ERROR,
                code=codes.UNKNOWN_ERROR,
                message="Unknown error occurred")

    return middle
