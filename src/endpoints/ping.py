"""ping module is used to test service
healthcheck by sending a GET /ping request
to the service this function should never
fail if the service is up"""

from src.common.standard import response
from src.common import codes


def ping():
    return response(code=codes.SUCCESS, message="pong")
