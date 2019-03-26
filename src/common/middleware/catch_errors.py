
import sys
import traceback

from http import HTTPStatus

from flask import request

from src.common import standard
from src.common import codes
from src.common import exceptions
from src.common import constants
from src.common.config import Config


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
            type, value, tb = sys.exc_info()
            print(type)
            print(value)
            traceback.print_tb(tb)
            return standard.error(http_status=HTTPStatus.INTERNAL_SERVER_ERROR, code=codes.UNKNOWN_ERROR, message="Unknown error occurred")

    return middle
