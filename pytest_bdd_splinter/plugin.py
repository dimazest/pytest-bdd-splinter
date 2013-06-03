"""Splinter subplugin for pytest-bdd."""

import pytest
import splinter


@pytest.fixture
def pytestbdd_close_browser():
    """Close browser fixture."""
    return True


@pytest.fixture
def pytestbdd_webdriver(request):
    """Webdriver fixture."""
    return request.config.option.pytestbdd_webdriver


@pytest.fixture
def browser(request, pytestbdd_close_browser, pytestbdd_webdriver):
    """Create splinter's browser for generic use."""
    browser = splinter.Browser(pytestbdd_webdriver)

    def fin():
        browser.quit()

    if pytestbdd_close_browser:
        request.addfinalizer(fin)

    return browser


def pytest_addoption(parser):
    parser.addoption(
        "--bdd-webdriver",
        help="pytest-bdd-splinter webdriver", type="choice", choices=splinter.browser._DRIVERS.keys(),
        dest='pytestbdd_webdriver', default='firefox')
