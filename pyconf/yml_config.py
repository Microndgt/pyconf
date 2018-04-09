import yaml
from .py_config import PyConfig


class YamlConfig(PyConfig):

    def load(self, config_file):
        with open(config_file) as config:
            config_obj = yaml.load(config)
        self._add_section_recursive(config_obj, self.sections['root'])
