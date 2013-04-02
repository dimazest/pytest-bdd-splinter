#!/usr/bin/env python
import os
from setuptools import setup, find_packages

packages = find_packages(os.path.dirname(os.path.abspath(__file__)))

setup(
    name='pytest-bdd-splinter',
    description='Splinter plugin for the pytest-bdd',
    version='0.1',
    install_requires=[
        'pytest-bdd',
    ],
    packages=packages,
)
