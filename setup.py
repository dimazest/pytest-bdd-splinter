#!/usr/bin/env python
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


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
