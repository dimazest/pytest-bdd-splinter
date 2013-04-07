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

