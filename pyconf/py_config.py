"""
Parsing python config file
"""
from .base_config import BaseConfig


class PyConfig(BaseConfig):
    def _add_section_recursive(self, conf_dict, last_section):
        for key, value in conf_dict.items():
            if isinstance(value, dict):
                current_section = self._add_section(key, last_section)
                self._add_section_recursive(value, current_section)
            else:
                self._add_dict_prop_to_section(key, value, section=last_section, pure=True)

    def load(self, config_file):
        config_obj = {}
        with open(config_file, mode='rb') as config:
            exec(config.read(), None, config_obj)
        self._add_section_recursive(config_obj, self.sections['root'])

