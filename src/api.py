

from src.flask_dragon.api import FlaskDragon
from src.common import middleware
from src.common.config import Config

from src.endpoints.upload import upload
from src.endpoints.ping import ping
from src.endpoints.list_all import list_all
from src.endpoints.remove import remove
from src.endpoints.update import update
from src.endpoints.find import find

Config.setup()

api = FlaskDragon("dragon-api")

api.middleware.add(middleware.catch_errors)

api.get('/api/ping', ping)
api.post('/api/v1/photos', upload)
api.get('/api/v1/photos', list_all)
api.put('/api/v1/photos/<string:id>', update)
api.get('/api/v1/photos/<string:id>', find)
api.delete('/api/v1/photos/<string:id>', remove)


if __name__ == '__main__':
    api.run(host='0.0.0.0')
