"""middleware module that manages all exceptions that
occur during the execution of an endpoint handler"""

from functools import wraps


def cors(handler):

    @wraps(handler)
    def middle(*args, **kwargs):

        response = handler(*args, **kwargs)
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

    return middle
