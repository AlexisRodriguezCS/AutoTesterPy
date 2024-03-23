"""
Test file for verifying test cases page on automationexercise.com.
"""
import pytest
from pages.header import HeaderLocators
from pages.test_cases_page import TestCasesLocators
from fixtures.conftest import browser


@pytest.mark.test
def test_test_cases_page(browser):
    """
    Test Case 7: Verify Test Cases Page

    Steps:
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Test Cases' button
        5. Verify user is navigated to test cases page successfully

    Args:
        browser (WebDriver): Instance of the browser.
    """
    # 4. Click on 'Test Cases' button
    header_page = HeaderLocators(browser)
    header_page.click_test_cases_button()

    # 5. Verify user is navigated to test cases page successfully
    test_cases_page = TestCasesLocators(browser)
    assert test_cases_page.verify_test_cases_text() is True
