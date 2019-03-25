

from src.flask_dragon.api import FlaskDragon
from src.common import middleware
from src.common.config import Config
from src.endpoints.upload import upload
from src.endpoints.ping import ping

Config.setup()

api = FlaskDragon("dragon-api")

api.middleware.add(middleware.catch_errors)

api.get('/api/ping', ping)
api.post('/api/v1/upload', upload)


if __name__ == '__main__':
    api.run(host='0.0.0.0')
