#!/usr/bin/env python
import os
from setuptools import setup, Command, find_packages


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys
        import subprocess
        errno = subprocess.call([sys.executable, '-m', 'pytest'])
        raise SystemExit(errno)

packages = find_packages(os.path.dirname(os.path.abspath(__file__)))

setup(
    name='pytest-bdd-splinter',
    description='Splinter subplugin for Pytest BDD plugin',
    version='0.1',
    cmdclass={'test': PyTest},
    install_requires=[
        'setuptools',
        'pytest-bdd',
        'splinter'
    ],
    tests_require=['mock'],
    entry_points={'pytest11': ['pytest-bdd-splinter=pytest_bdd_splinter.plugin']},
    packages=packages,
)
