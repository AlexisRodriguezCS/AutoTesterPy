"""
Module containing fixture for initializing the browser instance before running each test function.
"""
import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.home_page import HomePageLocators


@pytest.fixture(scope="function")
def browser():
    """
    Fixture to initialize the browser instance before running each test function.

    Returns:
        WebDriver: Instance of the browser.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Get the path to the Chrome executable from the environment variables
    chrome_path = os.getenv("CHROME_EXECUTABLE_PATH")

    # Initialize ChromeOptions
    chrome_options = Options()

    # Specify the path to the Chrome executable
    chrome_options.binary_location = chrome_path

    # Step 1: Launch browser with Chrome webdriver
    driver = webdriver.Chrome(options=chrome_options)

    # Step 2: Navigate to URL
    driver.get("http://automationexercise.com")

    # Step 3: Verify that home page is visible successfully
    home_page = HomePageLocators(driver)
    assert home_page.is_home_page_visible() is True

    yield driver

    # Teardown
    driver.quit()
