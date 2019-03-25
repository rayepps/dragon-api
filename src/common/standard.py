


from http import HTTPStatus

from flask import jsonify

from src.common import codes
from src.common.config import Config


def make_json_response(status, code, message, response):

    payload = {
        'code': code,
        'message': message,
        'version': Config.version
    }

    if response is not None:
        payload['response'] = response

    return payload

def response(http_status=HTTPStatus.OK, code=codes.SUCCESS, message=None, response=None):
    payload = make_json_response(http_status, code, message, response)
    return jsonify(payload), http_status

def error(http_status=HTTPStatus.INTERNAL_SERVER_ERROR, code=codes.UNKNOWN_ERROR, message=None, response=None):
    payload = make_json_response(http_status, code, message, response)
    return jsonify(payload), http_status
