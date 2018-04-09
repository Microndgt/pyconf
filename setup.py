from setuptools import setup

import pyconf

try:
    readme = open('README.md').read()
except:
    readme = 'pyconf: Configuration for Humans. Support ini config file, python config file'

setup(
    name=pyconf.__title__,
    version=pyconf.__version__,
    author=pyconf.__author__,
    description='Configuration for humans',
    long_description=readme,
    author_email='dgt_x@foxmail.com',
    url='https://github.com/Microndgt/pyconf',
    packages=['pyconf'],
    package_dir={'pyconf': 'pyconf'},
    package_data={'pyconf': ['*.conf']},
    include_package_data=True,
    license=pyconf.__license__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3']
    )
