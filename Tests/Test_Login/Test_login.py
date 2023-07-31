import time

import allure
import pytest
from Assets.Pages.Commons import Login
from Assets.Pages.Product_Page import ProductPage


@allure.epic('Test Valid Login')
@allure.id(1)
@allure.title("Insert Valid email and password and click LoginUp")
@allure.description('User will be logged in ')
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(driver):
    login = Login(driver)

    with allure.step('Insert valid Login credentials'):
        login.click_login()
        login.insert_user_name()
        login.insert_password()
        login.click_on_Enter_BTN()

    # Assertion: Verify that the user is successfully logged in
    assert login.is_logged_in(), "User was not logged in successfully"


@allure.epic('Test Invalid Login')
@allure.id(2)
@allure.title("Insert Invalid email and password and click LoginUp")
@allure.description('Error massage will appear ')
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(driver):
    login = Login(driver)

    with allure.step('Insert Invalid Login credentials'):
        login.click_login()
        login.insert_invalid_user_name()
        login.insert_invalid_password()
        login.click_on_Enter_BTN()

        # Assertion: Verify that an error message appears
    assert login.is_error_message_displayed(), "Error message did not appear"



