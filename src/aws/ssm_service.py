
import boto3
from werkzeug.utils import secure_filename

from src.common.config import Config
from src.common import constants
from src.common import validation
from src.aws import client as aws


class SSMService:

    @classmethod
    def get_api_key(cls):
        ssm_response = aws.ssm().get_parameter(Name='/dragon/api/apikey', WithDecryption=True)

        return ssm_response.get('Parameter').get('Value')
