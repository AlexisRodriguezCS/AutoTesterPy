"""
Module containing AccountDeletionPageLocators class for defining locators
and methods for account deletion page.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class AccountDeletionPageLocators(BasePage):
    """
    Locators and methods for the account deletion page.
    """

    ACCOUNT_DELETED_TEXT = (By.XPATH, "//h2[@data-qa='account-deleted']")
    CONTINUE_BUTTON = (By.XPATH, "//a[@data-qa='continue-button']")

    def verify_account_deleted_text(self):
        """
        Method to verify if the 'ACCOUNT DELETED!' text is visible on the page.

        Returns:
            bool: True if the text is visible, False otherwise.
        """
        return self.is_element_displayed(self.ACCOUNT_DELETED_TEXT)

    def click_continue_button(self):
        """Method to click on the Continue button."""
        self.click_element(self.CONTINUE_BUTTON)
