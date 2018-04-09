# pyconf

Configuration for Humans in ***Python3***.

**pyconf** is an INI/py/yml configuration parsing package, written for humans.

Installation
============

Install pyconf with pip:

```bash
pip install git+https://github.com/Microndgt/pyconf.git
```

Usage
=====

ini config file
---

```python
import pyconf
c = pyconf.load('tests/sample.conf', config_class=pyconf.IniConfig)
print(c['path'])
# some_path
```

python config file
---

```python
import pyconf
c = pyconf.load('tests/sample.py', config_class=pyconf.PyConfig)
print(c['path'])
# some_path
```

yaml config file
---

```python
import pyconf
c = pyconf.load('tests/sample.yml', config_class=pyconf.YamlConfig)
print(c['path'])
# some_path
```

Tests
=====

Run the tests with

```bash
python -m tests.test_ini_configs
python -m tests.test_py_configs
python -m tests.test_yaml_configs
```

History
===

0.1.1
---

1. support the yaml config file

0.1.0
---

1. change the Architecture
2. support the python config file

0.0.1
---

1. init project
2. ini config parser done
