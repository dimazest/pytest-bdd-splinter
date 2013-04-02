#!/usr/bin/env python
import os
from setuptools import setup, find_packages

packages = find_packages(os.path.dirname(os.path.abspath(__file__)))

setup(
    name='pytest-bdd-splinter',
    description='Splinter subplugin for Pytest BDD plugin',
    version='0.1',
    install_requires=[
        'pytest-bdd',
        'splinter'
    ],
    entry_points={'pytest11': ['pytest-bdd-splinter=pytest_bdd_splinter']},
    packages=packages,
)
