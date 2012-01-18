#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


APP_NAME = 'pyenv'
# APP_SCRIPT = './legit_r'
VERSION = '0.0.1'


# # Grab requirments.
# with open('reqs.txt') as f:
#     required = f.readlines()


settings = dict()


# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


settings.update(
    name=APP_NAME,
    version=VERSION,
    description='Python project environment tool.',
    long_description=open('README.rst').read(),
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/kennethreitz/pyenv',
    packages= ['pyenv',],
    # install_requires=required,
    license='BSD',
    classifiers=(
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
    entry_points={
        'console_scripts': [
            'pyenv = pyenv.cli:main',
        ],
    }
)



setup(**settings)
