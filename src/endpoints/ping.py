
from src.common.standard import response
from src.common import codes


def ping():
    return response(code=codes.SUCCESS, message="pong")
