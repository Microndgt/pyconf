"""
*******
pyconf
*******

**pyconf** is an INI/py/yml configuration parsing package, written for humans.

Usage
=====
Load a config file::

    >>> import pyconf
    >>> c = pyconf.load('tests/sample.conf')
    >>> c['general']
    {'foo': 'baz'}
"""

__title__ = 'pyconf'
__version__ = '0.1.0'
__author__ = 'Kevin Du'
__license__ = 'MIT'

from .ini_config import IniConfig
from .py_config import PyConfig
from .base_config import BaseConfig, Section
from .api import load
