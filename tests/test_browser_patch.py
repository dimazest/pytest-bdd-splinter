import time

from pytest_bdd_splinter.browser_patches import wait_until, WaitUntilTimeout

import pytest


def test_wait_until(
    browser,
    pytestbdd_browser_load_condition,
    pytestbdd_browser_load_timeout,
):
    """Test that by default wait_until is successful."""
    assert wait_until(
        browser,
        pytestbdd_browser_load_condition,
        pytestbdd_browser_load_timeout,
    )


def test_wait_until_timout(
    browser,
    monkeypatch,
):
    """Check timeouts."""
    ticks = iter([1, 2, 15])

    def fake_time():
        return next(ticks)

    monkeypatch.setattr(time, 'time', fake_time)

    assert wait_until(browser, lambda browser: False, 10)

    with pytest.raises(WaitUntilTimeout):
        wait_until(browser, lambda browser: False, 10)


def test_wait_until_condiiton(browser, monkeypatch):
    """Check conditioning."""
    checks = iter([False, True])

    def condition(browser):
        return next(checks)

    ticks = iter([1, 2, 3])

    def fake_time():
        return next(ticks)

    sleeps = []

    def fake_sleep(i):
        sleeps.append(i)

    monkeypatch.setattr(time, 'time', fake_time)
    monkeypatch.setattr(time, 'sleep', fake_sleep)

    assert wait_until(browser, condition, 10)

    assert sleeps == [0.1]
