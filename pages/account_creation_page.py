"""
Module containing AccountCreationPageLocators class for defining locators 
and methods for account creation page.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class AccountCreationPageLocators(BasePage):
    """
    Locators and methods for the account creation page.
    """
    # maybe the title
    ENTER_ACCOUNT_INFO_TITLE = (
        By.XPATH, '//*[@id="form"]/div/div/div/div/h2/b')
    TITLE_MR_RADIO = (By.ID, "id_gender1")
    TITLE_MRS_RADIO = (By.ID, "id_gender2")
    DOB_DAY_DROPDOWN = (By.ID, "days")
    DOB_MONTH_DROPDOWN = (By.ID, "months")
    DOB_YEAR_DROPDOWN = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    OFFERS_CHECKBOX = (By.ID, "optin")
    PASSWORD_INPUT = (By.ID, "password")
    FIRST_NAME_INPUT = (By.ID, "first_name")
    LAST_NAME_INPUT = (By.ID, "last_name")
    COMPANY_INPUT = (By.ID, "company")
    ADDRESS_INPUT = (By.ID, "address1")
    ADDRESS2_INPUT = (By.ID, "address2")
    COUNTRY_DROPDOWN = (By.ID, "country")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    ZIPCODE_INPUT = (By.ID, "zipcode")
    MOBILE_NUMBER_INPUT = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-qa='create-account']")

    def verify_account_info_text(self):
        """
        Method to verify if the 'ENTER ACCOUNT INFORMATION' text is visible on the page.

        Returns:
            bool: True if the text is visible, False otherwise.
        """
        return self.is_element_displayed(self.ENTER_ACCOUNT_INFO_TITLE)

    def select_title(self, title):
        """
        Method to select a title from the dropdown.

        Args:
            title (str): The title to select.
        """
        if title == 'Mr':
            self.click_element(self.TITLE_MR_RADIO)
        elif title == 'Mrs':
            self.click_element(self.TITLE_MRS_RADIO)

    def enter_account_details(self, password, dob_day, dob_month, dob_year):
        """
        Method to enter account details: Password and Date of Birth.

        Args:
            password (str): The password to enter.
            dob_day (str): The day of birth to select.
            dob_month (str): The month of birth to select.
            dob_year (str): The year of birth to select.
        """
        self.send_keys_to_element(self.PASSWORD_INPUT, password)
        self.send_keys_to_element(self.DOB_DAY_DROPDOWN, dob_day)
        self.send_keys_to_element(self.DOB_MONTH_DROPDOWN, dob_month)
        self.send_keys_to_element(self.DOB_YEAR_DROPDOWN, dob_year)

    def select_newsletter_and_offers(self):
        """Method to select newsletter and offers checkboxes."""
        self.click_element(self.NEWSLETTER_CHECKBOX)
        self.click_element(self.OFFERS_CHECKBOX)

    def fill_personal_details(
        self,
        first_name,
        last_name,
        company,
        address,
        address2,
        country,
        state,
        city,
        zipcode,
        mobile_number
    ):
        """
        Method to fill personal details.

        Args:
            first_name (str): The first name to enter.
            last_name (str): The last name to enter.
            company (str): The company name to enter.
            address (str): The address to enter.
            address2 (str): The address line 2 to enter.
            country (str): The country to select.
            state (str): The state to select.
            city (str): The city to enter.
            zipcode (str): The zipcode to enter.
            mobile_number (str): The mobile number to enter.
        """
        self.send_keys_to_element(self.FIRST_NAME_INPUT, first_name)
        self.send_keys_to_element(self.LAST_NAME_INPUT, last_name)
        self.send_keys_to_element(self.COMPANY_INPUT, company)
        self.send_keys_to_element(self.ADDRESS_INPUT, address)
        self.send_keys_to_element(self.ADDRESS2_INPUT, address2)
        self.send_keys_to_element(self.COUNTRY_DROPDOWN, country)
        self.send_keys_to_element(self.STATE_INPUT, state)
        self.send_keys_to_element(self.CITY_INPUT, city)
        self.send_keys_to_element(self.ZIPCODE_INPUT, zipcode)
        self.send_keys_to_element(self.MOBILE_NUMBER_INPUT, mobile_number)

    def click_create_account_button(self):
        """Method to click on the Create Account button."""
        self.click_element(self.CREATE_ACCOUNT_BUTTON)
