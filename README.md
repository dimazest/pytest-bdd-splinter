Splinter subpling for BDD library for the py.test runner
========================================================

[![Build Status](https://api.travis-ci.org/olegpidsadnyi/pytest-bdd-splinter.png)](https://travis-ci.org/olegpidsadnyi/pytest-bdd-splinter)

Install pytest-bdd-splinter
===========================

	pip install pytest-bdd-splinter

Features
========

The subplugin provides many useful fixtures to be used if you're using pytest-bdd for browser testing
(similar to Selenium2Library for Robotframework)

Fixtures
========

    *  browser -- get the splinter's Browser

    *  pytestbdd_selenium_implicit_wait -- implicit wait timeout to be passed to Selenium webdriver.
        Fixture gets the value from the command-line option bdd-selenium-implicit-wait (see below)

    *  pytestbdd_selenium_socket_timeout -- socket timeout for communication between the webdriver and the browser.
        Fixture gets the value from the command-line option bdd-socket-timeout (see below)

    *  pytestbdd_webdriver -- splinter's webdriver name to use. Fixture gets the value from the command-line option
        bdd-webdriver (see below)

Command-line options
====================

    *  --bdd-implicit-wait, seconds (default: 1) - the selenium webdriver implicit wait

    *  --bdd-socket-timeout, seconds (default: 600) - the selenium webdriver socket timeout for for communication
        between the webdriver and the browser

    *  --bdd-webdriver (default: firefox) - the webdriver name to use. Options:

        *  firefox
        *  remote
        *  chrome
        *  phantomjs

        For more details, refer to splinter and selenium documentation.

Example
=======

test_your_test.py:

    def test_some_browser_stuff(browser):
        """Test using real browser."""
        url = "http://www.google.com"
        browser.visit(url)
        browser.fill('q', 'splinter - python acceptance testing for web applications')
        # Find and click the 'search' button
        button = browser.find_by_name('btnK')
        # Interact with elements
        button.click()
        assert browser.is_text_present('splinter.cobrateam.info'), 'splinter.cobrateam.info wasn't found... We need to'
        ' improve our SEO techniques'

License
=======

This software is licensed under the [MIT license](http://en.wikipedia.org/wiki/MIT_License>).

© 2013 Oleg Pidsadnyi