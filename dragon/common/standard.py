"""standard module implements methods that should be
used to create/handle data in a standardized way across
the api such as response object shapes"""

from http import HTTPStatus
import json

from flask import Response as FlaskResponse

from dragon.common import codes
from dragon.common.types import JsonSerializable
from dragon.common.config import Config


def make_json_payload(status, code, message, body):

    payload = {
        'code': code,
        'message': message,
        'version': Config.version
    }

    if body is not None:
        payload['response'] = body

    return json.dumps(payload, default=JsonSerializable.serialize)

def make_response(http_status, code, message, body):

    payload = make_json_payload(http_status, code, message, body)

    res = FlaskResponse(response=payload, status=http_status, mimetype="application/json")
    res.headers["Content-Type"] = "application/json; charset=utf-8"

    return res

def response(http_status=HTTPStatus.OK, code=codes.SUCCESS, message=None, body=None):
    return make_response(http_status, code, message, body)

def error(http_status=HTTPStatus.INTERNAL_SERVER_ERROR, code=codes.UNKNOWN_ERROR, message=None, body=None):
    return make_response(http_status, code, message, body)
