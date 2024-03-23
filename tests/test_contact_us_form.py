"""
Test file for filling out Contact Us form on automationexercise.com.
"""
import os
import pytest
from dotenv import load_dotenv
from pages.home_page import HomePageLocators
from pages.header import HeaderLocators
from pages.contact_us_page import ContactFormLocators
from fixtures.conftest import browser

# Load environment variables from .env file
load_dotenv()


@pytest.mark.test
def test_contact_us_form(browser):
    """
    Test Case 6: Contact Us Form

    Steps:
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Contact Us' button
        5. Verify 'GET IN TOUCH' is visible
        6. Enter name, email, subject and message
        7. Upload file
        8. Click 'Submit' button
        9. Click OK button
        10. Verify success message 'Success! Your details have been submitted successfully.' 
            is visible
        11. Click 'Home' button and verify that landed to home page successfully

    Args:
        browser (WebDriver): Instance of the browser.
    """
    name = "Lorem"
    email = "lorem15@fake.com"
    subject = "Testing"
    message = "Lorem ipsum dolor sit amet."

    # Retrieve FILE_PATH from environment variables
    file_path = os.getenv("FILE_PATH")

    # 4. Click on 'Contact Us' button
    header_page = HeaderLocators(browser)
    header_page.click_contact_us_button()

    # 5. Verify 'GET IN TOUCH' is visible
    contact_us_page = ContactFormLocators(browser)
    assert contact_us_page.verify_get_in_touch_text() is True

    # 6. Enter name, email, subject and message
    contact_us_page.enter_message(name, email, subject, message)

    # 7. Upload file
    contact_us_page.upload_file(file_path)

    # 8. Click 'Submit' button
    # 9. Click OK button
    contact_us_page.submit_contact_form()

    # 10. Verify success message 'Success! Your details have been submitted successfully.'
    # is visible
    assert contact_us_page.verify_succes_message() is True

    # 11. Click 'Home' button and verify that landed to home page successfully
    contact_us_page.click_home_button()
    home_page = HomePageLocators(browser)
    assert home_page.is_home_page_visible() is True
