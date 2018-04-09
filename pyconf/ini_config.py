"""
Parsing ini config file
"""
import re
from os.path import abspath
from .base_config import BaseConfig


class IniConfig(BaseConfig):
    """Parsed configuration.

    Config instance includes a list of :class:`Section <configs.section.Section>` instances.
    """

    _comment = re.compile('^\s*;.*$')
    _header = re.compile('^\s*\[\s*(?P<section>\w+)\s*\]\s*$')
    _dict_item = re.compile('^\s*(?P<key>\w+)\s*\=\s*(?P<value>.+)\s*$')
    _list_item = re.compile('^\s*(?P<value>.+)\s*$')

    def load(self, config_file):
        """Parse an INI configuration file.

        :param config_file: configuration file to be loaded.
        """

        current_section = None

        with open(config_file) as f:
            for line in f.readlines():
                comment_match = re.match(self._comment, line)
                if comment_match:
                    continue

                header_match = re.match(self._header, line)
                if header_match:
                    current_section = header_match.group('section')
                    if current_section not in self.sections:
                        self._add_section(current_section)

                    continue

                dict_item_match = re.match(self._dict_item, line)
                if dict_item_match:
                    key, value = dict_item_match.group('key'), dict_item_match.group('value')

                    if current_section:
                        self._add_dict_prop_to_section(key, value, self.sections[current_section])
                    else:
                        self._add_dict_prop_to_section(key, value)

                    continue

                list_item_match = re.match(self._list_item, line)
                if list_item_match:
                    value = list_item_match.group('value')
                    if current_section:
                        self._add_list_prop_to_section(value, self.sections[current_section])
                    else:
                        self._add_list_prop_to_section(value)

                    continue

            self.config_full_path = abspath(f.name)
