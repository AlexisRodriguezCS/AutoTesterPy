"""
Module containing TestCasesLocators class for defining locators and methods for 
the Test Cases page.
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage


class TestCasesLocators(BasePage):
    """
    Locators and methods for the Test Cases page.
    """
    test_cases_text = (By.XPATH, "//h2[contains(., 'Test Cases')]")

    def verify_test_cases_text(self):
        """
        Verify if the 'TEST CASES' is displayed on the page.

        Returns:
            bool: True if the text is displayed, False otherwise.
        """
        return self.is_element_displayed(self.test_cases_text)
