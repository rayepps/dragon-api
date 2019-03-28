import json
import unittest
from unittest.mock import MagicMock, patch

from src.common.config import Config

# SUT
from src.aws import client


def mock_client_creator(name, endpoint_url=None):
    return name, endpoint_url

class TestClient(unittest.TestCase):

    def test_client_s3_gets_local(self):

        with patch('src.aws.client.boto3.client', side_effect=mock_client_creator):
            name, endpoint = client.s3()
            self.assertEqual(name, 's3')
            self.assertEqual(endpoint, Config.s3_url)

    def test_client_ssm_gets_local(self):

        with patch('src.aws.client.boto3.client', side_effect=mock_client_creator):
            name, endpoint = client.ssm()
            self.assertEqual(name, 'ssm')
            self.assertEqual(endpoint, Config.ssm_url)

    def test_client_dynamo_gets_local(self):

        with patch('src.aws.client.boto3.resource', side_effect=mock_client_creator):
            name, endpoint = client.dynamo()
            self.assertEqual(name, 'dynamodb')
            self.assertEqual(endpoint, Config.dynamo_url)

    def test_client_s3(self):

        Config.exec_env = 'not_local'

        with patch('src.aws.client.boto3.client', side_effect=mock_client_creator):
            name, endpoint = client.s3()
            self.assertEqual(name, 's3')
            self.assertEqual(endpoint, None)

        Config.exec_env = 'local'

    def test_client_ssm(self):

        Config.exec_env = 'not_local'

        with patch('src.aws.client.boto3.client', side_effect=mock_client_creator):
            name, endpoint = client.ssm()
            self.assertEqual(name, 'ssm')
            self.assertEqual(endpoint, None)

        Config.exec_env = 'local'

    def test_client_dynamo(self):

        Config.exec_env = 'not_local'

        with patch('src.aws.client.boto3.resource', side_effect=mock_client_creator):
            name, endpoint = client.dynamo()
            self.assertEqual(name, 'dynamodb')
            self.assertEqual(endpoint, None)

        Config.exec_env = 'local'
