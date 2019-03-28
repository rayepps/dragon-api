import json
import unittest

import requests

from test.integration.util.base import IntegrationTestCase


class TestPingEndpoint(IntegrationTestCase):

    def test_gets_pong(self):

        res = requests.get(f'{self.endpoint}/api/ping').json()

        self.assertEqual(res['message'], 'pong')
