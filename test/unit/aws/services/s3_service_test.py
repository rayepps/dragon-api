import json
import unittest
from unittest.mock import MagicMock, patch

from src.common.config import Config
from src.common import exceptions

# SUT
from src.aws.services import s3


class TestS3Service(unittest.TestCase):

    @patch('src.aws.services.s3.aws')
    def test_s3_service_calls_put_object(self, aws_mock):

        s3_mock = MagicMock()
        put_object_mock = MagicMock()
        s3_mock.put_object = put_object_mock
        aws_mock.s3 = MagicMock(return_value=s3_mock)

        s3.upload(None, None)

        put_object_mock.assert_called()

    @patch('src.aws.services.s3.aws')
    def test_s3_service_calls_remove(self, aws_mock):

        delete_mock = MagicMock()
        object_mock = MagicMock()
        object_mock.delete = delete_mock
        s3_mock = MagicMock()
        s3_mock.Object = MagicMock(return_value=object_mock)
        aws_mock.s3 = MagicMock(return_value=s3_mock)

        s3.remove(None)

        delete_mock.assert_called()

    @patch('src.aws.services.s3.aws')
    @patch('src.aws.services.s3.constants')
    def test_s3_service_generates_url(self, constants_mock, aws_mock):

        constants_mock.S3_BUCKET_NAME = 'yolo'

        s3_mock = MagicMock()
        s3_mock.meta = MagicMock()
        s3_mock.meta.endpoint_url = 'barbaz'
        aws_mock.s3 = MagicMock(return_value=s3_mock)

        res = s3.generate_url('gogo')

        self.assertEqual(res, 'barbaz/yolo/gogo')
