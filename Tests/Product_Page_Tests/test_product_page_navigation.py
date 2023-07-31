import time
import allure
import pytest
from Assets.Pages.Product_Page import ProductPage


@allure.epic('Test Navigation to the kids section')
@allure.id(1)
@allure.title("Choosing the kids section")
@allure.description('Kids products will display')
@allure.severity(allure.severity_level.MINOR)
def test_navigation_to_the_kids_section(driver):
    PP = ProductPage(driver)
    with allure.step('Click on the product button and navigate to the kids section'):
        PP.Click_On_Products_Section()
        PP.Click_On_Kids_And_Babies_Section()
        PP.Click_On_Kids_Section()

        # Get the current URL
        current_url = driver.current_url
        expected_url = 'https://www.ikea.com/il/he/cat/children-bc003/'

        # Assert that the current URL matches the expected URL
        assert current_url == expected_url, "The current URL does not match the expected URL"


@allure.epic('Test Filtering price high to low')
@allure.id(2)
@allure.title("Choosing Price low to high filter")
@allure.description('Kids products will appear in the desired order')
@allure.severity(allure.severity_level.NORMAL)
def test_filter_price_low_to_high(driver):
    PP = ProductPage(driver)
    with allure.step('Click on the product button and navigate to the kids section'):
        PP.Click_On_Products_Section()
        PP.Click_On_Kids_And_Babies_Section()
        PP.Click_On_Kids_Section()
        time.sleep(5)

    with allure.step('Choosing the filter low to high price'):
        PP.Click_On_Filter_Button()
        PP.Click_On_Low_To_High_Price()
        time.sleep(5)

        # Get the current URL
        current_url = driver.current_url
        expected_url = 'https://www.ikea.com/il/he/cat/children-bc003/?sort=PRICE_LOW_TO_HIGH'

        # Assert that the current URL matches the expected URL
        assert current_url == expected_url, "The current URL does not match the expected URL"


@allure.epic('Test Filtering category Toys for kids')
@allure.id(3)
@allure.title("Choosing Toys for kids category")
@allure.description('Kids products will appear in the desired category')
@allure.severity(allure.severity_level.NORMAL)
def test_Toys_for_kids_products(driver):
    PP = ProductPage(driver)
    with allure.step('Click on the product button and navigate to the kids section'):
        PP.Click_On_Products_Section()
        PP.Click_On_Kids_And_Babies_Section()
        PP.Click_On_Kids_Section()
        time.sleep(5)

    with allure.step('Choosing the Toys for kids category'):
        PP.Click_On_Category_Button()
        PP.Click_On_Toys_For_Kids_Option()

        # Get the current URL
        current_url = driver.current_url
        expected_url = 'https://www.ikea.com/il/he/cat/children-bc003/?filters=f-subcategories%3A18734'

        # Assert that the current URL matches the expected URL
        assert current_url == expected_url, "The current URL does not match the expected URL"


@allure.epic('Test Filtering Green products')
@allure.id(4)
@allure.title("Choosing Green kids products")
@allure.description('Kids Green products will appear')
@allure.severity(allure.severity_level.NORMAL)
def test_filter_green_products(driver):
    PP = ProductPage(driver)
    with allure.step('Click on the product button and navigate to the kids section'):
        PP.Click_On_Products_Section()
        PP.Click_On_Kids_And_Babies_Section()
        PP.Click_On_Kids_Section()
        time.sleep(5)

    with allure.step('Choosing the Green products filter'):
        PP.Click_On_Color_filter_Btn()
        PP.Click_On_Green()
        time.sleep(5)

        # Get the current URL
        current_url = driver.current_url
        expected_url = 'https://www.ikea.com/il/he/cat/children-bc003/?filters=f-colors%3A10033'

        # Assert that the current URL matches the expected URL
        assert current_url == expected_url, "The current URL does not match the expected URL"


@allure.epic('Test Navigating to the bedroom section')
@allure.id(4)
@allure.title("Choosing Room, Bedrooms")
@allure.description('Bedrooms products will appear')
@allure.severity(allure.severity_level.NORMAL)
def test_filter_green_products(driver):
    PP = ProductPage(driver)
    with allure.step('Click on the rooms btn at the homepage'):
        PP.CLick_On_Rooms()
        PP.Click_On_Bedrooms()

    # Get the current URL
    current_url = driver.current_url
    expected_url = 'https://www.ikea.com/il/he/rooms/bedroom/'

    # Assert that the current URL matches the expected URL
    assert current_url == expected_url, "The current URL does not match the expected URL"



