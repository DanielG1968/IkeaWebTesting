import time

import allure
import pytest
from Assets.Pages.Commons import Login
from Assets.Pages.Product_Page import ProductPage
from Assets.Pages.Personal_Area import PersonalArea


@allure.epic('Test Edit Personal details')
@allure.id(1)
@allure.title("Edit the personal details")
@allure.description('Personal details will be changed')
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(driver):
    login = Login(driver)
    PA = PersonalArea(driver)

    with allure.step('Insert valid Login credentials'):
        login.click_login()
        login.insert_user_name()
        login.insert_password()
        login.click_on_Enter_BTN()

    with allure.step('Entering the personal area page and editing the data'):
        PA.click_on_my_profile()
        PA.click_edit_personal_info_BTN()
        PA.insert_new_name()
        PA.insert_new_last_name()
        PA.insert_birth_year()
        PA.insert_birth_month()
        PA.insert_birth_day()
        PA.click_on_save_BTN()

    # Assertion: Verify that the personal details are successfully saved
    assert PA.is_personal_details_saved(), "Personal details were not saved successfully"