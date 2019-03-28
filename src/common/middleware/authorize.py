"""authorize module wraps an endpoint handler and
requires some form of validated authorization before
allowing the handler to execute"""

from functools import wraps

from flask import request

from src.common import exceptions


def authorize(api_key):

    def wrapper(handler):

        @wraps(handler)
        def require_api_key(*args, **kwargs):
            if 'x-api-key' not in request.headers:
                raise exceptions.missing_header.add('x-api-key')
            key = request.headers['x-api-key']
            if key != api_key:
                raise exceptions.unauthorized

            return handler(*args, **kwargs)

        return require_api_key

    return wrapper
