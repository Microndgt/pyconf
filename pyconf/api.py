from .ini_config import IniConfig
from .py_config import PyConfig


support_configs = (IniConfig, PyConfig)


def load(config_file, config_class=IniConfig):
    """Constructs and returns a :class:`Config <Config>` instance.

    :param config_file: configuration file to be parsed
    :param ext: configuration extension

    Usage::

        >>> import pyconf

        >>> fc = pyconf.load('tests/sample.conf')

        >>> fc['general']['spam']
    """
    # ini extensions
    if config_class not in support_configs:
        raise Exception("config class: {} not supported".format(config_class))
    configs = {}
    try:
        configs = config_class(config_file)
    except FileNotFoundError:
        raise
    except Exception as e:
        for extra_config_class in support_configs:
            if config_class == extra_config_class:
                continue
            try:
                configs = extra_config_class(config_file)
            except FileNotFoundError:
                raise
            else:
                return configs
    return configs
