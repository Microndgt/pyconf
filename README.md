# pyconf

Configuration for Humans

**Configs** is an INI/py/yml configuration parsing package, written for humans.

Installation
============

Install configs with pip:

```bash
pip install git+https://github.com/Microndgt/pyconf.git
```

Usage
=====
Load a config file

```python
import pyconf
c = pyconf.load('sample.conf')
print(c['general'])
# {'foo': 'baz'}
```

Tests
=====

Run the tests with

```bash
python test_configs.py
```
