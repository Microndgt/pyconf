from .ini_config import IniConfig


config_parsers = {
    'ini': IniConfig
}


def load(config_file, ext="ini"):
    """Constructs and returns a :class:`Config <Config>` instance.

    :param config_file: configuration file to be parsed
    :param ext: configuration extension

    Usage::

        >>> import pyconf

        >>> fc = pyconf.load('sample.conf')

        >>> fc['general']['spam']
    """
    # ini extensions
    Config = config_parsers.get(ext, 'ini')
    configs = {}
    try:
        configs = Config(config_file)
    except FileNotFoundError:
        raise
    except Exception as e:
        for extension, config_class in config_parsers.items():
            if Config == config_class:
                continue
            try:
                configs = config_class(config_file)
            except FileNotFoundError:
                raise
            else:
                return configs
    return configs
