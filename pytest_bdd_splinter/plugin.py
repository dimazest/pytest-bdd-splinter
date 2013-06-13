"""Splinter subplugin for pytest-bdd."""

import pytest
import splinter

from .webdriver_patches import patch_webdriver
from .splinter_patches import patch_webdriverelement


@pytest.fixture
def pytestbdd_close_browser():
    """Close browser fixture."""
    return True


@pytest.fixture
def pytestbdd_webdriver(request):
    """Webdriver fixture."""
    return request.config.option.pytestbdd_webdriver


@pytest.fixture
def pytestbdd_selenium_socket_timeout(request):
    """Internal Selenium socket timeout (communication between webdriver and the browser).
    :return: Seconds.
    """
    return request.config.option.pytestbdd_webdriver_socket_timeout


@pytest.fixture
def pytestbdd_selenium_implicit_wait(request):
    """Selenium implicit wait timeout.
    :return: Seconds.
    """
    return request.config.option.pytestbdd_webdriver_implicit_wait


@pytest.fixture
def browser(
        request, pytestbdd_selenium_socket_timeout, pytestbdd_selenium_implicit_wait,
        pytestbdd_close_browser, pytestbdd_webdriver):
    """Splinter browser wrapper instance. To be used for browser interaction."""
    patch_webdriver(pytestbdd_selenium_socket_timeout)
    patch_webdriverelement()
    browser = splinter.Browser(pytestbdd_webdriver)
    browser.driver.implicitly_wait(pytestbdd_selenium_implicit_wait)

    def fin():
        browser.quit()

    if pytestbdd_close_browser:
        request.addfinalizer(fin)
    return browser


def pytest_addoption(parser):
    """Pytest hook to add custom command line option(s)."""
    parser.addoption(
        "--bdd-webdriver",
        help="pytest-bdd-splinter webdriver", type="choice", choices=splinter.browser._DRIVERS.keys(),
        dest='pytestbdd_webdriver', default='firefox')

    parser.addoption(
        "--bdd-implicit-wait",
        help="pytest-bdd-splinter selenium implicit wait, seconds", type="int",
        dest='pytestbdd_webdriver_implicit_wait', default=1)

    parser.addoption(
        "--bdd-socket-timeout",
        help="pytest-bdd-splinter socket timeout, seconds", type="int",
        dest='pytestbdd_webdriver_socket_timeout', default=600)
