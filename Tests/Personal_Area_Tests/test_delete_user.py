import allure
import pytest
from Assets.Pages.Commons import Login
from Assets.Pages.Product_Page import ProductPage
from Assets.Pages.Personal_Area import PersonalArea


@allure.epic('Test valid delete user')
@allure.id(1)
@allure.title("insert valid password and delete user")
@allure.description('User will be deleted')
@allure.severity(allure.severity_level.NORMAL)
def test_valid_login(driver):
    login = Login(driver)
    PA = PersonalArea(driver)

    with allure.step('Insert valid Login credentials'):
        login.click_login()
        login.insert_user_name()
        login.insert_password()
        login.click_on_Enter_BTN()

    with allure.step('selecting the delete user section and deleting the account'):
        PA.click_on_delete_user_section()
        PA.insert_valid_delete_user_password()
        PA.click_on_delete_account()

        # Add an assertion to verify the deletion was successful
        assert PA.is_account_deleted(), "User account deletion was not successful"


@allure.epic('Test invalid delete user')
@allure.id(2)
@allure.title("insert invalid password and delete user")
@allure.description('Error massage wil display')
@allure.severity(allure.severity_level.NORMAL)
def test_valid_login(driver):
    login = Login(driver)
    PA = PersonalArea(driver)

    with allure.step('Insert valid Login credentials'):
        login.click_login()
        login.insert_user_name()
        login.insert_password()
        login.click_on_Enter_BTN()

    with allure.step('selecting the delete user section and deleting the account'):
        PA.click_on_delete_user_section()
        PA.insert_invalid_delete_user_password()
        PA.click_on_delete_account()

        # Add an assertion to verify the error message is displayed
        assert PA.is_error_message_displayed(), "Error message is not displayed for invalid password"
