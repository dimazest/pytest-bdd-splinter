"""Patches for splinter"""

from selenium.webdriver.common.action_chains import ActionChains
from splinter.driver.webdriver.firefox import WebDriverElement

def patch_webdriverelement():
    """Patches the WebDriverElement to allow firefox to use mouse_over"""
    def mouse_over(self):
        """Performs a mouse over the element."""
        ActionChains(self.parent.driver).move_to_element(self._element).perform()


    # Apply the monkey patch for Firefox WebDriverElement
    WebDriverElement.mouse_over = mouse_over
