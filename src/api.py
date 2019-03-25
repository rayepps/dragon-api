
from flask import Flask

from src.endpoints.upload import upload
from src.endpoints.ping import ping


api = Flask(__name__)

api.route('/api/v1/ping', methods=['GET'])(ping)
api.route('/api/v1/upload', methods=['POST'])(upload)







if __name__ == '__main__':
    api.run(host='0.0.0.0')
