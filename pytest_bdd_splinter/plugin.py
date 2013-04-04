"""Splinter subplugin for pytest-bdd."""

import pytest
import splinter


@pytest.fixture
def browser(request):
    """Create splinter's browser for generic use."""
    browser = splinter.Browser()

    def fin():
        browser.quit()
    request.addfinalizer(fin)

    return browser
