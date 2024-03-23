"""
Test file for logging out user on automationexercise.com.
"""
import pytest
from pages.header import HeaderLocators
from pages.auth_page import AuthPageLocators
from fixtures.conftest import browser


@pytest.mark.test
def test_logout_user(browser):
    """
    Test Case 4: Logout User

    Steps:
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'Login to your account' is visible
        6. Enter correct email address and password
        7. Click 'login' button
        8. Verify that 'Logged in as username' is visible
        9. Click 'Logout' button
        10. Verify that user is navigated to login page

    Args:
        browser (WebDriver): Instance of the browser.
    """
    username = "Test"
    email_input = "random123@fake.com"
    password_input = "password123"

    # 4. Click on 'Signup / Login' button
    header_page = HeaderLocators(browser)
    header_page.click_signup_login_button()

    # 5. Verify 'Login to your account' is visible
    auth_page = AuthPageLocators(browser)
    assert auth_page.verify_login_to_your_account_text() is True

    # 6. Enter correct email address and password
    auth_page.enter_email_and_password(email_input, password_input)

    # 7. Click 'login' button
    auth_page.click_login_button()

    # 8. Verify that 'Logged in as username' is visible
    assert header_page.verify_logged_in_text(username) is True

    # 9. Click 'Logout' button
    header_page.click_logout_button()

    # 10. Verify that user is navigated to login page
    assert auth_page.verify_login_to_your_account_text() is True
