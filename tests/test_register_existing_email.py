"""
Test file for regiserting user with existing email on automationexercise.com.
"""
import pytest
from pages.header import HeaderLocators
from pages.auth_page import AuthPageLocators
from fixtures.conftest import browser


@pytest.mark.test
def test_register_existing_email(browser):
    """
    Test Case 5: Register User with existing email

    Steps:
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'New User Signup!' is visible
        6. Enter name and already registered email address
        7. Click 'Signup' button
        8. Verify error 'Email Address already exist!' is visible

    Args:
        browser (WebDriver): Instance of the browser.
    """
    username = "Test"
    email_input = "random123@fake.com"

    # 4. Click on 'Signup / Login' button
    header_page = HeaderLocators(browser)
    header_page.click_signup_login_button()

    # 5. Verify 'New User Signup!' is visible
    auth_page = AuthPageLocators(browser)
    assert auth_page.verify_new_user_signup_text() is True

    # 6. Enter name and already registered email address
    auth_page.enter_name_and_email(username, email_input)

    # 7. Click 'Signup' button
    auth_page.click_signup_button()

    # 8. Verify error 'Email Address already exist!' is visible
    assert auth_page.verify_email_exist_text() is True
