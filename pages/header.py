"""
Module containing HeaderLocators class for defining locators and methods for the main page.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class HeaderLocators(BasePage):
    """
    Locators and methods for the main page.
    """
    SIGNUP_LOGIN_BUTTON = (
        By.XPATH, "//a[@href='/login' and contains(., 'Signup / Login')]")
    LOGGED_IN_TEXT = (By.XPATH, "//a[text()='Logged in as']")
    DELETE_ACCOUNT_BUTTON = (
        By.XPATH, "//a[contains(@href, '/delete_account')]")
    LOGOUT_BUTTON = (
        By.XPATH, "//a[contains(@href, '/logout') and contains(., 'Logout')]")
    CONTACT_US_BUTTON = (
        By.XPATH, "//a[contains(@href, '/contact_us') and text()=' Contact us']")
    test_cases_button = (
        By.XPATH, "//a[contains(@href, '/test_cases') and text()=' Test Cases']")

    def click_signup_login_button(self):
        """
        Click on the Signup / Login button.
        """
        self.click_element(self.SIGNUP_LOGIN_BUTTON)

    def verify_signup_login_button_displayed(self):
        """
        Verify if the Signup / Login button is displayed on the page.

        Returns:
            bool: True if the button is displayed, False otherwise.
        """
        return self.is_element_displayed(self.SIGNUP_LOGIN_BUTTON)

    def verify_logged_in_text(self, username):
        """
        Verify if the 'Logged in as username' text is visible on the page.

        Args:
            username (str): The username to verify.

        Returns:
            bool: True if the text is visible, False otherwise.
        """
        xpath = f"//a[contains(text(), 'Logged in as')]/b[contains(text(), '{username}')]"
        return self.is_element_displayed((By.XPATH, xpath))

    def click_delete_account_button(self):
        """
        Click on the Delete Account button.
        """
        self.click_element(self.DELETE_ACCOUNT_BUTTON)

    def click_logout_button(self):
        """
        Click on the Logout button.
        """
        self.click_element(self.LOGOUT_BUTTON)

    def click_contact_us_button(self):
        """
        Click on the contact us button.
        """
        self.click_element(self.CONTACT_US_BUTTON)

    def click_test_cases_button(self):
        """
        Click on the test cases button.
        """
        self.click_element(self.test_cases_button)
