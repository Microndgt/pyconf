import unittest

from pyconf import api
from pyconf import IniConfig
from typing import Sequence


class TestIniConfig(unittest.TestCase):

    def setUp(self):
        self.sample_config_filename = 'tests/sample.conf'
        self.missing_config_filename = 'missing.conf'

    def test_load_general(self):
        """Check if a valid config file is parsed correctly"""

        self.assertIsInstance(api.load(self.sample_config_filename, config_class=IniConfig), IniConfig)

    def test_load_missing_file(self):
        """Check if the correct exception in raised when a missing config file is attempted to parse"""

        with self.assertRaises(FileNotFoundError):
            api.load(self.missing_config_filename)

    def test_load_check_types(self):
        """Check automatic float, integer, and boolean value conversion"""
        config_data = api.load(self.sample_config_filename, config_class=IniConfig)
        self.assertIsInstance(config_data['path'], str)
        self.assertIsInstance(config_data['hosts'], Sequence)
        self.assertIsInstance(config_data['hosts'][0], str)

        self.assertIsInstance(config_data['list_section'][0], float)
        self.assertIsInstance(config_data['list_section'][1], int)
        self.assertIsInstance(config_data['list_section'][2], tuple)

        self.assertIsInstance(config_data['list_section'][2][0], str)
        self.assertIsInstance(config_data['list_section'][2][1], int)

        self.assertIsInstance(config_data['mixed']['boolean'], bool)
        self.assertIsInstance(config_data['mixed']['list'], tuple)

        self.assertIsInstance(config_data['mixed']['list'][0], float)


if __name__ == '__main__':
    unittest.main()
