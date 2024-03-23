"""
Module containing AccountCreationSuccessPageLocators class for defining locators 
and methods for account creation success page.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class AccountCreationSuccessPageLocators(BasePage):
    """
    Locators and methods for the account creation success page.
    """

    ACCOUNT_CREATED_TEXT = (By.XPATH, "//h2[@data-qa='account-created']")
    CONTINUE_BUTTON = (By.XPATH, "//a[@data-qa='continue-button']")

    def verify_account_created_text(self):
        """
        Method to verify if the 'ACCOUNT CREATED!' text is visible on the page.

        Returns:
            bool: True if the text is visible, False otherwise.
        """
        return self.is_element_displayed(self.ACCOUNT_CREATED_TEXT)

    def click_continue_button(self):
        """Method to click on the Continue button."""
        self.click_element(self.CONTINUE_BUTTON)
