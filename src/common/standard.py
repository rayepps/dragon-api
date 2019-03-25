


from http import HTTPStatus
import json

from flask import Response

from src.common import codes
from src.common.types import JsonSerializable
from src.common.config import Config


def make_json_payload(status, code, message, response):

    payload = {
        'code': code,
        'message': message,
        'version': Config.version
    }

    if response is not None:
        payload['response'] = response

    return json.dumps(payload, default=JsonSerializable.serialize)

def make_response(http_status, code, message, response):

    payload = make_json_payload(http_status, code, message, response)

    r = Response(response=payload, status=http_status, mimetype="application/json")
    r.headers["Content-Type"] = "application/json; charset=utf-8"

    return r

def response(http_status=HTTPStatus.OK, code=codes.SUCCESS, message=None, response=None):
    return make_response(http_status, code, message, response)

def error(http_status=HTTPStatus.INTERNAL_SERVER_ERROR, code=codes.UNKNOWN_ERROR, message=None, response=None):
    return make_response(http_status, code, message, response)
