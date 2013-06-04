"""Selenium webdriver monkey patches.

Patches are temporary fixes for issues raised in we selenium google project:
http://code.google.com/p/selenium/issues/detail?id=5175
http://code.google.com/p/selenium/issues/detail?id=5176.
"""

import os
import socket

from selenium.webdriver.remote import webelement, remote_connection
from selenium.webdriver.firefox import webdriver


class LocalFileDetector(object):
    """Overriden LocalFileDetector to inject correct file_path check."""

    @classmethod
    def is_local_file(cls, *keys):
        file_path = ''
        typing = []
        for val in keys:
            if isinstance(val, webelement.Keys):
                typing.append(val)
            elif isinstance(val, int):
                val = str(val)
                for i in range(len(val)):
                    typing.append(val[i])
            else:
                for i in range(len(val)):
                    typing.append(val[i])
        file_path = ''.join(typing)

        if file_path is '':
            return None

        try:
            # we added os.path.isabs(file_path) to ensure it's path and not just string
            if os.path.isabs(file_path) and os.path.exists(file_path):
                return file_path
        except:
            pass
        return None


# Get the original _request and store for future use in the monkey patched version as 'super'
old_request = remote_connection.RemoteConnection._request


def patch_webdriver(selenium_timeout):

    def _request(*args, **kwargs):
        """Override _request to set socket timeout to some appropriate value."""
        timeout = socket.getdefaulttimeout()
        try:
            socket.setdefaulttimeout(selenium_timeout)
            return old_request(*args, **kwargs)
        finally:
            socket.setdefaulttimeout(timeout)

    # Apply the monkey patche for RemoteConnection
    remote_connection.RemoteConnection._request = _request
    # Apply the monkey patch for LocalFileDetector
    webelement.LocalFileDetector = LocalFileDetector

    # Apply the monkey patch to Firefox webdriver to disable native events
    # to avoid click on wrong elements, totally unpredictable
    # more info http://code.google.com/p/selenium/issues/detail?id=633
    webdriver.WebDriver.NATIVE_EVENTS_ALLOWED = False
