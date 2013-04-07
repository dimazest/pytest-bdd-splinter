#!/usr/bin/env python
from setuptools import setup, Command


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

setup(
    name='pytest-bdd-splinter',
    description='Splinter subplugin for Pytest BDD plugin',
    author='Oleg Pidsadnyi, Anatoly Bubenkov',
    version='0.1',
    cmdclass={'test': PyTest},
    install_requires=[
        'setuptools',
        'pytest-bdd',
        'splinter'
    ],
    tests_require=['mock'],
    entry_points={'pytest11': ['pytest-bdd-splinter=pytest_bdd_splinter.plugin']},
    packages=['pytest_bdd_splinter'],
)
