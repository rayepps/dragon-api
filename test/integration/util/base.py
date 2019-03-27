import json
import unittest
from os import environ as env


class IntegrationTestCase(unittest.TestCase):

    _endpoint = None

    @property
    def endpoint(self):
        if IntegrationTestCase._endpoint is None:
            IntegrationTestCase._endpoint = env['INTEGRATION_TEST_HOST']
        return IntegrationTestCase._endpoint
