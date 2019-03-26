
import sys
import traceback

from http import HTTPStatus

from flask import request

from src.common import standard
from src.common import codes
from src.common import exceptions
from src.common import constants
from src.common.config import Config



def authorize(handler):

    def require_api_key(*args, **kwargs):
        if 'x-api-key' not in request.headers:
            raise exceptions.missing_header('x-api-key')
        api_key = request.headers['x-api-key']
        if api_key != Config.api_key:
            raise exceptions.unauthorized
        return handler(*args, **kwargs)

    return require_api_key
