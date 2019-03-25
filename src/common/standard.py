


from http import HTTPStatus

from flask import jsonify

from src.common import codes


def response(http_status=HTTPStatus.OK, code=codes.SUCCESS, message=None, response=None):

    payload = {
        'code': code,
        'message': message
    }

    if response is not None:
        payload['response'] = response

    return jsonify(payload), http_status
