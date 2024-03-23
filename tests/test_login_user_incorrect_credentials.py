"""
Test file for logging in with incorrect email and password on automationexercise.com.
"""
import pytest
from pages.header import HeaderLocators
from pages.auth_page import AuthPageLocators
from fixtures.conftest import browser


@pytest.mark.test
def test_login_user_incorrect_credentials(browser):
    """
    Test Case 3: Login User with incorrect email and password

    Steps:
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'Login to your account' is visible
        6. Enter incorrect email address and password
        7. Click 'login' button
        8. Verify error 'Your email or password is incorrect!' is visible

    Args:
        browser (WebDriver): Instance of the browser.
    """
    email_input = "random@fake.com"
    password_input = "password123"

    # 4. Click on 'Signup / Login' button
    header_page = HeaderLocators(browser)
    header_page.click_signup_login_button()

    # 5. Verify 'Login to your account' is visible
    auth_page = AuthPageLocators(browser)
    assert auth_page.verify_login_to_your_account_text() is True

    # 6. Enter incorrect email address and password
    auth_page.enter_email_and_password(email_input, password_input)

    # 7. Click 'login' button
    auth_page.click_login_button()

    # 8. Verify error 'Your email or password is incorrect!' is visible
    assert auth_page.verify_incorrect_text() is True

    # Test completed
    print("Test Case 3 Completed: Login User with incorrect email and password")
