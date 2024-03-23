"""
Module containing ContactFormLocators class for defining locators and methods for 
the contact us page.
"""
import os
import autoit
from selenium.webdriver.common.by import By
from .base_page import BasePage


class ContactFormLocators(BasePage):
    """
    Locators and methods for the contact us page.
    """
    get_in_touch_text = (By.XPATH, "//h2[contains(text(), 'Get In Touch')]")
    name_input = (By.CSS_SELECTOR, "input[data-qa='name']")
    email_input = (By.CSS_SELECTOR, "input[data-qa='email']")
    subject_input = (By.CSS_SELECTOR, "input[data-qa='subject']")
    message_textarea = (By.CSS_SELECTOR, "textarea[data-qa='message']")
    upload_file_input = (By.CSS_SELECTOR, "input[name='upload_file']")
    submit_button = (By.CSS_SELECTOR, "input[data-qa='submit-button']")
    success_message = (
        By.CSS_SELECTOR, "div.status.alert.alert-success")
    home_button = (By.CSS_SELECTOR, "a.btn.btn-success")

    def submit_contact_form(self):
        """
        Submit contact form and handle the JavaScript alert.
        """
        self.click_button(self.submit_button)
        self.handle_alert(accept=True)

    def verify_get_in_touch_text(self):
        """
        Verify if the 'GET IN TOUCH' is displayed on the page.

        Returns:
            bool: True if the text is displayed, False otherwise.
        """
        return self.is_element_displayed(self.get_in_touch_text)

    def verify_succes_message(self):
        """
        Verify if the 'Success! Your details have been submitted successfully.' 
        is displayed on the page.

        Returns:
            bool: True if the text is displayed, False otherwise.
        """
        return self.is_element_displayed(self.success_message)

    def enter_message(self, name: str, email: str, subject: str, message: str):
        """Method to enter name, email, subject, and message in the respective input fields."""
        self.enter_data(self.name_input, name)
        self.enter_data(self.email_input, email)
        self.enter_data(self.subject_input, subject)
        self.enter_data(self.message_textarea, message)

    def upload_file(self, file_path: str):
        """
        Upload a file using the Windows system explorer pop-up.

        Args:
            file_path (str): Path to the file to be uploaded.
        """
        self.logger.info("Uploading file: %s", file_path)

        # Clicking on the upload input to trigger the file explorer
        self.click_button(self.upload_file_input)

        # Wait for the file dialog to appear
        autoit.win_wait_active("Open")

        # Set the file path in the file dialog
        autoit.control_set_text("Open", "Edit1", os.path.abspath(file_path))

        # Click the Open button to upload the file
        autoit.control_click("Open", "Button1")

    def click_home_button(self):
        """Method to click on the Home button."""
        self.click_button(self.home_button)
