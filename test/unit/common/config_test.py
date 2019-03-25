import json
import unittest

from src.common.config import Config

class TestConfig(unittest.TestCase):

    def test_config(self):

        Config.setup()

        self.assertTrue(Config.version != 'unknown')
