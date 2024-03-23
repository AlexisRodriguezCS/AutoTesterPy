"""
Module containing BasePage class for defining locators and methods for the Base page.
"""

import logging
from typing import Tuple
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver


class Config:
    """
    Configuration class for common settings.
    """
    WAIT_TIME = 30
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOG_LEVEL = logging.INFO


class BasePage:
    """
    Base class for page objects.
    """

    def __init__(self, driver: WebDriver, wait_time: int = Config.WAIT_TIME):
        """
        Initialize BasePage class.

        Args:
            driver: WebDriver instance.
            wait_time (int): Maximum time to wait for elements (default is 30 seconds).
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(Config.LOG_LEVEL)

    def find_element(self, locator: Tuple[str, str]):
        """
        Find element based on locator.

        Args:
            locator: Tuple (By, value) representing locator strategy and value.

        Returns:
            WebElement: Element found using the locator.

        Raises:
            TimeoutException: If element is not found within specified time.
        """
        self.logger.info("Finding element: %s", locator)
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.logger.error("Element not found within specified time.")
            raise

    def click_element(self, locator: Tuple[str, str]):
        """
        Click on element based on locator.

        Args:
            locator: Tuple (By, value) representing locator strategy and value.
        """
        self.logger.info("Clicking element: %s", locator)
        element = self.find_element(locator)
        element.click()

    def send_keys_to_element(self, locator: Tuple[str, str], keys: str):
        """
        Send keys to element based on locator.

        Args:
            locator: Tuple (By, value) representing locator strategy and value.
            keys (str): Keys to send to the element.
        """
        self.logger.info("Sending keys '%s' to element: %s", keys, locator)
        element = self.find_element(locator)
        element.send_keys(keys)

    def get_element_text(self, locator: Tuple[str, str]) -> str:
        """
        Get text of element based on locator.

        Args:
            locator: Tuple (By, value) representing locator strategy and value.

        Returns:
            str: Text of the element.
        """
        self.logger.info("Getting text of element: %s", locator)
        return self.find_element(locator).text

    def is_element_displayed(self, locator: Tuple[str, str]) -> bool:
        """
        Check if element is displayed based on locator.

        Args:
            locator: Tuple (By, value) representing locator strategy and value.

        Returns:
            bool: True if the element is displayed, False otherwise.
        """
        self.logger.info("Checking if element is displayed: %s", locator)
        try:
            return self.find_element(locator).is_displayed()
        except TimeoutException:
            return False

    def verify_text(self, locator: Tuple[str, str]) -> bool:
        """
        Method to verify if the specified text element is visible on the page.

        Args:
            locator: Tuple (By, value) representing locator strategy and value.

        Returns:
            bool: True if the text is visible, False otherwise.
        """
        self.logger.info("Verifying text: %s", locator)
        return self.is_element_displayed(locator)

    def enter_data(self, locator: Tuple[str, str], data: str):
        """
        Method to enter data into the specified input field.

        Args:
            locator: Tuple (By, value) representing locator strategy and value.
            data (str): The data to enter.
        """
        self.logger.info("Entering data '%s' into element: %s", data, locator)
        self.send_keys_to_element(locator, data)

    def click_button(self, locator: Tuple[str, str]):
        """
        Method to click on the specified button.

        Args:
            locator: Tuple (By, value) representing locator strategy and value.
        """
        self.logger.info("Clicking button: %s", locator)
        self.click_element(locator)

    def handle_alert(self, accept=True):
        """
        Handle JavaScript alert.

        Args:
            accept (bool): Whether to accept (True) or dismiss (False) the alert. 
            Default is True (accept).
        """
        try:
            alert = self.wait.until(EC.alert_is_present())
            if accept:
                alert.accept()
            else:
                alert.dismiss()
            self.logger.info("Alert handled successfully.")
        except TimeoutException:
            self.logger.error("No alert present.")
            raise
