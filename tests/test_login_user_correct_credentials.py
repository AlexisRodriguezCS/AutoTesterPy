"""
Test file for logging in with correct email and password on automationexercise.com.
"""
import pytest
from pages.header import HeaderLocators
from pages.auth_page import AuthPageLocators
from pages.account_deletion_page import AccountDeletionPageLocators
from fixtures.conftest import browser


@pytest.mark.test
def test_login_user_correct_credentials(browser):
    """
    Test Case 2: Login User with correct email and password

    Steps:
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'Login to your account' is visible
        6. Enter correct email address and password
        7. Click 'login' button
        8. Verify that 'Logged in as username' is visible
        9. Click 'Delete Account' button
        10. Verify that 'ACCOUNT DELETED!' is visible

    Args:
        browser (WebDriver): Instance of the browser.
    """
    username = "Alexis"
    email_input = "alexisrodriguezdev123@fake.com"
    password_input = "password123"

    # Step 4: Click on 'Signup / Login' button
    header_page = HeaderLocators(browser)
    header_page.click_signup_login_button()

    # Step 5: Verify 'Login to your account' is visible
    auth_page = AuthPageLocators(browser)
    assert auth_page.verify_login_to_your_account_text() is True

    # Step 6: Enter correct email address and password
    auth_page.enter_email_and_password(email_input, password_input)

    # Step 7: Click 'login' button
    auth_page.click_login_button()

    # Step 8: Verify that 'Logged in as username' is visible
    assert header_page.verify_logged_in_text(username) is True

    # Step 9: Click 'Delete Account' button
    header_page.click_delete_account_button()

    # Step 10: Verify that 'ACCOUNT DELETED!' is visible
    account_deletion_page = AccountDeletionPageLocators(browser)
    assert account_deletion_page.verify_account_deleted_text() is True

    # Test completed
    print("Test Case 2 Completed: Login User with correct email and password.")
