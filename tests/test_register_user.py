"""
Test file for user registration flow on automationexercise.com.
"""
import pytest
from pages.header import HeaderLocators
from pages.auth_page import AuthPageLocators
from pages.account_creation_page import AccountCreationPageLocators
from pages.account_creation_success_page import AccountCreationSuccessPageLocators
from pages.account_deletion_page import AccountDeletionPageLocators
from fixtures.conftest import browser


@pytest.mark.test
def test_register_user(browser):
    """
    Test Case 1:  Register User.

    Steps:
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'New User Signup!' is visible
        6. Enter name and email address
        7. Click 'Signup' button
        8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
        9. Fill details: Title, Name, Email, Password, Date of birth
        10. Select checkbox 'Sign up for our newsletter!'
        11. Select checkbox 'Receive special offers from our partners!'
        12. Fill details: First name, Last name, Company, Address, Address2,
          Country, State, City, Zipcode, Mobile Number
        13. Click 'Create Account button'
        14. Verify that 'ACCOUNT CREATED!' is visible
        15. Click 'Continue' button
        16. Verify that 'Logged in as username' is visible
        17. Click 'Delete Account' button
        18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button

    Args:
        browser (WebDriver): Instance of the browser.
    """
    # Step 4: Click on 'Signup / Login' button
    header_page = HeaderLocators(browser)
    header_page.click_signup_login_button()

    # Step 5: Verify 'New User Signup!' is visible
    auth_page = AuthPageLocators(browser)
    assert auth_page.verify_new_user_signup_text() is True

    # Step 6: Enter name and email address
    auth_page.enter_name_and_email("Test", "qatester123456@example.com")

    # Step 7: Click 'Signup' button
    auth_page.click_signup_button()

    # Step 8: Verify 'ENTER ACCOUNT INFORMATION' is visible
    account_creation_page = AccountCreationPageLocators(browser)
    assert account_creation_page.verify_account_info_text() is True

    # Step 9: Fill details: Title, Name, Email, Password, Date of birth
    account_creation_page.select_title("Mr")
    account_creation_page.enter_account_details(
        "Password123", "01", "January", "2000")

    # Step 10: Select checkbox 'Sign up for our newsletter!'
    # Step 11: Select checkbox 'Receive special offers from our partners!'
    account_creation_page.select_newsletter_and_offers()

    # Step 12: Fill details:
    # First name, Last name, Company,
    # Address, Address2, Country, State, City, Zipcode, Mobile Number
    account_creation_page.fill_personal_details(
        "Alexis", "Rodriguez", "SWE Inc", "123 Main St", "Apt 404",
        "United States", "Illinois", "Chicago", "60804",
        "1234567890")

    # Step 13: Click 'Create Account' button
    account_creation_page.click_create_account_button()

    # Step 14: Verify 'ACCOUNT CREATED!' is visible
    account_creation_success_page = AccountCreationSuccessPageLocators(browser)
    assert account_creation_success_page.verify_account_created_text() is True

    # Step 15: Click 'Continue' button
    account_creation_success_page.click_continue_button()

    # Step 16: Verify 'Logged in as username' is visible
    assert header_page.verify_logged_in_text("Test") is True

    # Step 17: Click 'Delete Account' button
    header_page.click_delete_account_button()

    # Step 18: Verify 'ACCOUNT DELETED!' is visible
    account_deletion_page = AccountDeletionPageLocators(browser)
    assert account_deletion_page.verify_account_deleted_text() is True

    # Step 19: Click 'Continue' button
    account_deletion_page.click_continue_button()

    # Test completed
    print("Test completed")
