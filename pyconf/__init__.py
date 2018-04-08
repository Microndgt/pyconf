"""
*******
Configs
*******

**Configs** is an INI/py/yml configuration parsing package, written for humans.

Usage
=====
Load a config file::

    >>> import pyconf
    >>> c = pyconf.load('sample.conf')
    >>> c['general']
    {'foo': 'baz'}
"""

__title__ = 'pyconf'
__version__ = '0.0.1'
__author__ = 'Kevin Du'
__license__ = 'MIT'

from .ini_config import IniConfig
from .api import load
