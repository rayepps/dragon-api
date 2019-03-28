"""ssm service module manages fetching keys from ssm service"""

from src.aws import client as aws


class SSMService:

    @classmethod
    def get_api_key(cls):
        ssm_response = aws.ssm().get_parameter(Name='/dragon/api/apikey', WithDecryption=True)

        return ssm_response.get('Parameter').get('Value')
