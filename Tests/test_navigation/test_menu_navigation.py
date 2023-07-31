import time
import pytest
import allure
from Assets.Pages.Menu_Page import MenuPage


@allure.epic('Test navigating to the Inspirations and ideas section, Welcome to my home')
@allure.id(1)
@allure.title("Navigating to the Menu then to the inspirations and ideas section and clicking the welcome to my home "
              "btn")
@allure.description('Welcome to my home page will display')
@allure.severity(allure.severity_level.NORMAL)
def test_navigation_to_the_kids_section(driver):
    MP = MenuPage(driver)
    with allure.step('Click on the Menu, Inspirations and ideas, Welcome to my home'):
        MP.Click_On_Menu_BTN()
        MP.Click_On_Inspirations_and_ideas_Section()
        MP.Click_On_Inspirations_And_Ideas_Welcome_To_my_Home()

        current_url = driver.current_url
        expected_url = 'https://www.ikea.com/il/he/ideas/welcome-to-my-place/'

        assert current_url == expected_url, 'The current URL does not match the expected URL'


@allure.epic('Test navigating to the Inspirations and ideas section, Bedroom')
@allure.id(2)
@allure.title("Navigating to the Menu then to the inspirations and ideas section and clicking the bedroom "
              "btn")
@allure.description('Bedroom page will display')
@allure.severity(allure.severity_level.NORMAL)
def test_navigation_to_the_kids_section(driver):
    MP = MenuPage(driver)
    with allure.step('Click on the Menu, Inspirations and ideas, Bedroom'):
        MP.Click_On_Menu_BTN()
        MP.Click_On_Inspirations_and_ideas_Section()
        MP.Click_On_Inspirations_And_Ideas_Bedroom()

        # Assertion: Check if the product image container is visible
        product_image_container = MP.Product_is_visible()
        assert product_image_container, "Product image container is not displayed on the Bedroom page"

