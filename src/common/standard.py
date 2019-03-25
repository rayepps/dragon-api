


from http import HTTPStatus

from flask import jsonify

from src.common import codes
from src.common.config import Config


def response(http_status=HTTPStatus.OK, code=codes.SUCCESS, message=None, response=None):

    payload = {
        'code': code,
        'message': message,
        'version': Config.version
    }

    if response is not None:
        payload['response'] = response

    return jsonify(payload), http_status
