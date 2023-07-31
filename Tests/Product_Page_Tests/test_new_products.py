import time
import allure
import pytest
from Assets.Pages.Product_Page import ProductPage


@allure.epic('Verify that the product AVSTEG is being displayed on the new products section')
@allure.id(1)
@allure.title("Navigating to the new products section")
@allure.description('AVSTEG will display')
@allure.severity(allure.severity_level.MINOR)
def test_navigation_to_the_kids_section(driver):
    PP = ProductPage(driver)
    with allure.step('Click on the New products section and verify AVSTEG is displayed'):
        PP.Click_On_New_Products()
        displayed_products = PP.get_displayed_products()  # Assuming this method returns a list of displayed product
        # names
        assert "AVSTEG" in displayed_products, "AVSTEG is not displayed on the new products section"
