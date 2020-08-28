"""ping module is used to test service
healthcheck by sending a GET /ping request
to the service this function should never
fail if the service is up"""

from dragon.common.standard import response
from dragon.common import codes


def ping():
    return response(code=codes.SUCCESS, message="pong")
