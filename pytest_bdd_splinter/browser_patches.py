"""Browser patches."""
import time


def wait_until(browser, condition, timeout=10):
    """Wait until the condition becomes false or the timeout happens.

    :param condition: a callable that takes no parameters, returns a boolean.
    :param timeout: the timout time

    """
    max_time = time.time() + timeout

    while not condition(browser):
        if time.time() > max_time:
            raise Exception('Timeout')

        time.sleep(0.1)


class WaitUntilTimeout(Exception):
    """Thrown when the timeout happened during waiting for a condition."""
