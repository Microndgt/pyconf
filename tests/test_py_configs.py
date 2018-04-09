import unittest

from pyconf import api, PyConfig, Section
from typing import Sequence


class TestPyConfig(unittest.TestCase):

    def setUp(self):
        self.sample_config_filename = 'tests/sample.py'
        self.missing_config_filename = 'missing.py'

    def test_load_general(self):
        """Check if a valid config file is parsed correctly"""

        self.assertIsInstance(api.load(self.sample_config_filename, config_class=PyConfig), PyConfig)

    def test_load_missing_file(self):
        """Check if the correct exception in raised when a missing config file is attempted to parse"""

        with self.assertRaises(FileNotFoundError):
            api.load(self.missing_config_filename)

    def test_load_check_types(self):
        """Check automatic float, integer, and boolean value conversion"""
        config_data = api.load(self.sample_config_filename, config_class=PyConfig)
        self.assertIsInstance(config_data['path'], str)
        self.assertIsInstance(config_data['hosts'], Sequence)
        self.assertIsInstance(config_data['hosts'][0], str)

        self.assertIsInstance(config_data['section'], Section)
        self.assertIsInstance(config_data['section']['attr1'], float)
        self.assertIsInstance(config_data['section']['attr2'], int)
        self.assertIsInstance(config_data['section']['foo'], int)

        self.assertIsInstance(config_data['section2'], Section)
        self.assertIsInstance(config_data['section2']['attr1'], float)
        self.assertIsInstance(config_data['section2']['attr2'], int)
        self.assertIsInstance(config_data['section2']['foo'], int)
        self.assertIsInstance(config_data['section2']['inner_section'], Section)
        self.assertIsInstance(config_data['section2']['inner_section']['two'], int)
        self.assertIsInstance(config_data['section2']['inner_section']['test_section'], Section)
        self.assertIsInstance(config_data['section2']['inner_section']['test_section'][1], int)


if __name__ == '__main__':
    unittest.main()
