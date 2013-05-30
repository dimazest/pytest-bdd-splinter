"""Splinter subplugin for pytest-bdd."""

import pytest
import splinter


@pytest.fixture
def pytestbdd_close_browser():
    """Close browser fixture."""
    return True


@pytest.fixture
def pytestbdd_webdriver():
    """Webdriver fixture."""
    return 'firefox'


@pytest.fixture
def browser(request, pytestbdd_close_browser, pytestbdd_webdriver):
    """Create splinter's browser for generic use."""
    browser = splinter.Browser(pytestbdd_webdriver)

    def fin():
        browser.quit()

    if pytestbdd_close_browser:
        request.addfinalizer(fin)

    return browser
