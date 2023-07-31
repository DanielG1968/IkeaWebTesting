import time

import allure
import pytest
from Assets.Pages.Commons import Login
from Assets.Pages.Product_Page import ProductPage


@allure.epic('Test Valid SignUp')
@allure.id(1)
@allure.title("Insert Valid email and password and click signUp")
@allure.description('User will be signed Up')
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(driver):
    login = Login(driver)

    with allure.step('Insert valid sign up credentials'):
        login.click_login()
        login.click_on_Create_User()
        login.insert_first_name()
        login.insert_last_name()
        login.insert_new_email()
        login.insert_new_password()
        time.sleep(5)
        login.click_on_info_and_updated_checkbox()
        login.click_on_privacy_policy_checkbox()
        login.click_on_create_account()

    assert login.is_logged_in(), "User was not logged in successfully"


