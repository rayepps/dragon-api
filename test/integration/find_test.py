import json
import unittest

import requests

from test.integration.util.base import IntegrationTestCase

from src.common import codes


class TestFindEndpoint(IntegrationTestCase):

    def test_get_invalid_todo_id_returns_error(self):

        todo_id = 'notarealtodoid'

        res = requests.get(f'{self.endpoint}/api/v1/todos/{todo_id}', headers={ 'x-api-key': 'localhashkey' }).json()

        self.assertEqual(res['code'], codes.TODO_NOT_FOUND)
