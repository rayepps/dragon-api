"""api is the main starting point for the dragon
service. This module does the work of importing
all endpoint handlers and middleware and configuring
it all on the flask application router"""

from src.flask_dragon.api import FlaskDragon

from src.common.middleware.authorize import authorize
from src.common.middleware.catch_errors import catch_errors
from src.common.config import Config
from src.aws.services import ssm

from src.endpoints.create import create
from src.endpoints.ping import ping
from src.endpoints.list_all import list_all
from src.endpoints.remove import remove
from src.endpoints.update import update
from src.endpoints.find import find
from src.endpoints.attach import attach
from src.endpoints.detatch import detatch


def run():

    api = FlaskDragon("dragon-api")

    # Order matters here

    # Add the error catching middleware before
    # anything else so all else gets caught
    api.middleware.add(catch_errors)

    # Add the ping handler
    api.get('/api/ping', ping)

    # Add the authorize middleware - this will
    # apply to everything we add to come
    api_key = ssm.get('/dragon/api/apikey')
    authorizer = authorize(api_key)
    api.middleware.add(authorizer)

    api.post('/api/v1/todos', create)
    api.get('/api/v1/todos', list_all)
    api.put('/api/v1/todos/<string:todo_id>', update)
    api.get('/api/v1/todos/<string:todo_id>', find)
    api.delete('/api/v1/todos/<string:todo_id>', remove)

    api.post('/api/v1/todos/<string:todo_id>/attach', attach)
    api.delete('/api/v1/todos/<string:todo_id>/detatch', detatch)


    api.run(host='0.0.0.0')

if __name__ == '__main__':
    Config.setup()
    run()
