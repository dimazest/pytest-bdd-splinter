"""Tests for pytest-bdd-splinter subplugin."""

import mock
import splinter
from splinter.driver.webdriver.firefox import WebDriver

mocked_browser = mock.MagicMock()
splinter.Browser = lambda *args, **kwargs: mocked_browser


def test_browser(request, browser):
    assert browser is mocked_browser
    assert request._pyfuncitem.session._setupstate._finalizers

    with mock.patch.object(WebDriver, 'quit') as mocked:
        request._pyfuncitem.session._setupstate._finalizers.values()[0][0]()
        assert mocked.assert_called_once()
