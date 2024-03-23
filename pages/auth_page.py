"""
Module containing AuthPageLocators class for defining locators and methods for authentication page.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class AuthPageLocators(BasePage):
    """
    Locators and methods for the authentication page.
    """

    LOGIN_TO_YOUR_ACCOUNT_TEXT = (
        By.XPATH, "//div[@class='login-form']//h2[contains(text(),'Login to your account')]")
    EMAIL_LOGIN = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_LOGIN = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    INCORRECT_TEXT = (
        By.XPATH, "//p[contains(text(), 'Your email or password is incorrect!')]")
    EMAIL_EXIST_TEXT = (
        By.XPATH, "//p[contains(., 'Email Address already exist!')]")
    NEW_USER_SIGNUP_TEXT = (
        By.XPATH, "//div[@class='signup-form']//h2[contains(text(),'New User Signup!')]")
    NAME_SIGNUP = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    EMAIL_ADDRESS_SIGNUP = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    def verify_new_user_signup_text(self) -> bool:
        """Method to verify if the 'New User Signup!' text is visible on the page."""
        return self.verify_text(self.NEW_USER_SIGNUP_TEXT)

    def verify_login_to_your_account_text(self) -> bool:
        """Method to verify if the 'Login to your account' text is visible on the page."""
        return self.verify_text(self.LOGIN_TO_YOUR_ACCOUNT_TEXT)

    def verify_incorrect_text(self) -> bool:
        """Method to verify if the 'Your email or password is incorrect!'
        text is visible on the page."""
        return self.verify_text(self.INCORRECT_TEXT)

    def verify_email_exist_text(self) -> bool:
        """Method to verify if the 'Email Address already exist!'
        text is visible on the page."""
        return self.verify_text(self.EMAIL_EXIST_TEXT)

    def enter_email_and_password(self, email: str, password: str):
        """Method to enter email and password in the respective input fields."""
        self.enter_data(self.EMAIL_LOGIN, email)
        self.enter_data(self.PASSWORD_LOGIN, password)

    def enter_name_and_email(self, name: str, email: str):
        """Method to enter name and email in the respective input fields."""
        self.enter_data(self.NAME_SIGNUP, name)
        self.enter_data(self.EMAIL_ADDRESS_SIGNUP, email)

    def click_signup_button(self):
        """Method to click on the Signup button."""
        self.click_button(self.SIGNUP_BUTTON)

    def click_login_button(self):
        """Method to click on the Login button."""
        self.click_button(self.LOGIN_BUTTON)
