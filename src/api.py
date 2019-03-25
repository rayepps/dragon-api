
from flask import Flask

from src.common.config import Config
from src.endpoints.upload import upload
from src.endpoints.ping import ping

Config.setup()

api = Flask(__name__)

api.route('/api/ping', methods=['GET'])(ping)
api.route('/api/v1/upload', methods=['POST'])(upload)



if __name__ == '__main__':
    api.run(host='0.0.0.0')
