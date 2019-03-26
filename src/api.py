
from src.flask_dragon.api import FlaskDragon

from src.common.middleware.authorize import authorize
from src.common.middleware.catch_errors import catch_errors
from src.common.config import Config

from src.endpoints.upload import upload
from src.endpoints.ping import ping
from src.endpoints.list_all import list_all
from src.endpoints.remove import remove
from src.endpoints.update import update
from src.endpoints.find import find

Config.setup()

api = FlaskDragon("dragon-api")

# Order matters here

# Add the error catching middleware before
# anything else so all else gets caught
api.middleware.add(catch_errors)

# Add the ping handler
api.get('/api/ping', ping)

# Add the authorize middleware - this will
# apply to everything we add to come
api.middleware.add(authorize)

api.post('/api/v1/photos', upload)
api.get('/api/v1/photos', list_all)
api.put('/api/v1/photos/<string:id>', update)
api.get('/api/v1/photos/<string:id>', find)
api.delete('/api/v1/photos/<string:id>', remove)


if __name__ == '__main__':
    api.run(host='0.0.0.0')
