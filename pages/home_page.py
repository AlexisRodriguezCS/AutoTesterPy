"""
Module containing HomePageLocators class for defining locators and methods for 
the Home page.
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePageLocators(BasePage):
    """
    Locators and methods for the Home page.
    """
    slider_carousel = (By.ID, "slider-carousel")

    def is_home_page_visible(self):
        """
        Verify if the Slider Carousel is displayed on the page.

        Returns:
            bool: True if the silder carousel is displayed, False otherwise.
        """
        return self.is_element_displayed(self.slider_carousel)
