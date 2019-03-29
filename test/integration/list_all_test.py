import json
import unittest

import requests

from test.integration.util.base import IntegrationTestCase


class TestListAllEndpoint(IntegrationTestCase):

    def test_success(self):

        res = requests.get(f'{self.endpoint}/api/v1/todos')
