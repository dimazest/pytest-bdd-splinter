#!/usr/bin/env python
"""
PyTest-BDD-Splinter
===================

The subplugin provides many useful fixtures to be used if you're using pytest-bdd for
browser testing (similar to Selenium2Library for Robotframework).

Fixtures
````````

browser -- get the splinter's Browser

- pytestbdd_selenium_implicit_wait -- implicit wait timeout to be passed to Selenium webdriver.
    Fixture gets the value from the command-line option bdd-selenium-implicit-wait (see below)

- pytestbdd_selenium_socket_timeout -- socket timeout for communication between the webdriver and the browser.
    Fixture gets the value from the command-line option bdd-socket-timeout (see below)

- pytestbdd_webdriver -- splinter's webdriver name to use. Fixture gets the value from the command-line option
    bdd-webdriver (see below)


Example
```````

test_your_test.py:

.. code:: python

    def test_some_browser_stuff(browser):
        # Test using real browser
        url = "http://www.google.com"
        browser.visit(url)
        browser.fill('q', 'splinter - python acceptance testing for web applications')

        # Find and click the 'search' button
        button = browser.find_by_name('btnK')

        # Interact with elements
        button.click()
        assert browser.is_text_present('splinter.cobrateam.info'), 'splinter.cobrateam.info wasn't found... We need to'
        ' improve our SEO techniques'

Installation
````````````

.. code:: bash

    $ pip install pytest-bdd-splinter

Links
`````

* `website <https://github.com/olegpidsadnyi/pytest-bdd-splinter>`_
* `documentation <https://pytest-bdd-splinter.readthedocs.org/en/latest/>`_

"""

import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # The import is here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='pytest-bdd-splinter',
    description='Splinter subplugin for Pytest BDD plugin',
    long_description=__doc__,
    author='Oleg Pidsadnyi',
    license='MIT license',
    author_email='oleg.podsadny@gmail.com',
    version='0.4.2-dev',
    cmdclass={'test': PyTest},
    url='https://github.com/olegpidsadnyi/pytest-bdd-splinter',
    install_requires=[
        'setuptools',
        'pytest-bdd',
        'splinter',
    ],
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ] + [('Programming Language :: Python :: %s' % x) for x in '2.6 2.7 3.0 3.1 3.2 3.3'.split()],
    tests_require=['mock'],
    entry_points={'pytest11': ['pytest-bdd-splinter=pytest_bdd_splinter.plugin']},
    packages=['pytest_bdd_splinter'],
)
