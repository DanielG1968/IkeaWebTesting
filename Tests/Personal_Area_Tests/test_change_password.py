import time

import allure
import pytest
from Assets.Pages.Commons import Login
from Assets.Pages.Product_Page import ProductPage
from Assets.Pages.Personal_Area import PersonalArea


@allure.epic('Test Edit the password')
@allure.id(1)
@allure.title("Edit the password with valid credentials")
@allure.description('Password will be changed')
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(driver):
    login = Login(driver)
    PA = PersonalArea(driver)

    with allure.step('Insert valid Login credentials'):
        login.click_login()
        login.insert_user_name()
        login.insert_password()
        login.click_on_Enter_BTN()

    with allure.step('Edit the password'):
        PA.click_on_change_password_BTN()
        PA.insert_current_password()
        PA.insert_new_password()
        PA.confirm_new_password()
        PA.click_on_save_new_password()

    # Assertion: Verify that the password is successfully changed
    assert PA.is_password_changed(), "Password was not changed successfully"

