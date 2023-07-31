import allure
import pytest
from Assets.Pages.Commons import Login
from Assets.Pages.Product_Page import ProductPage
from Assets.Pages.Personal_Area import PersonalArea


@allure.epic('Test Edit Preferred ikea store ')
@allure.id(1)
@allure.title("Choosing the ראשון לציון store")
@allure.description('Preferred store will be changed')
@allure.severity(allure.severity_level.MINOR)
def test_valid_login(driver):
    login = Login(driver)
    PA = PersonalArea(driver)

    with allure.step('Insert valid Login credentials'):
        login.click_login()
        login.insert_user_name()
        login.insert_password()
        login.click_on_Enter_BTN()

    with allure.step('Change the preferred store'):
        PA.click_on_preferred_store()
        PA.click_on_choose_store()
        PA.choose_Rishon_Le_Zion_Store()

    # After changing the preferred store
    current_preferred_store = PA.get_preferred_store_name()
    expected_preferred_store = "ראשון לציון"  # Update with the expected store name

    assert current_preferred_store == expected_preferred_store, \
        f"Preferred store is not set correctly. Expected: {expected_preferred_store}, Actual: {current_preferred_store}"


