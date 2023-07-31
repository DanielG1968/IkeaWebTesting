import os
import Assets.Pages.Utils as U
from Assets.Pages.Commons import Commons
import pyautogui


# Creating Personal Area locators
class PersonalArea(Commons):
    My_profile = (U.By.CSS_SELECTOR, '#pp-skapa__main-page-navigation-0 > button > '
                                     'span.pp-skapa__list-view-item__control-icon > svg')
    Edit_Personal_INFO_BTN = (U.By.CSS_SELECTOR, '#root > div > main > div.grid_gridLeft__0Kzru.profile-details'
                                                 '-page_wrapperLeft__DI1yA > '
                                                 'div.profile-details-content-left_basicInfoWrapper__YfST0 > '
                                                 'div.profile-details-content-left_headerArea__Wt48H > button')
    Edit_first_name = (U.By.CSS_SELECTOR, '#first-name')

    Edit_Last_name = (U.By.CSS_SELECTOR, '#last-name')

    Edit_Birth_year = (U.By.CSS_SELECTOR, '#date-of-birth-year')

    Edit_Birth_month = (U.By.CSS_SELECTOR, '#date-of-birth-month')

    Edit_Birth_Day = (U.By.CSS_SELECTOR, '#date-of-birth-day')

    SAVE_BTN = (U.By.CSS_SELECTOR, '#edit-profile-modal > div:nth-child(3) > div > '
                                   'div.pp-skapa__modal-footer.pp-skapa__modal-footer--borderless.pp-skapa__modal'
                                   '-footer--dual-action > '
                                   'button.pp-skapa__btn.pp-skapa__btn--primary.pp-skapa__btn--fluid')

    Change_password_BTN = (U.By.CSS_SELECTOR, '#divPreChatButton > button.remove-launcher.cb-close-icon-btn')
    Current_Password = (U.By.CSS_SELECTOR, '#divPreChatButton > button.remove-launcher.cb-close-icon-btn')
    Edit_New_Password = (U.By.CSS_SELECTOR, '#new-password')
    Confirm_New_Password = (U.By.CSS_SELECTOR, '#new-confirmed-password')
    Confrim_passsword_button = (U.By.CSS_SELECTOR, '#root > div > main > '
                                                   'div.grid_gridLeft__0Kzru.change-password_content__rVxIp > form > '
                                                   'button')
    Preferred_Ikea_store = (U.By.CSS_SELECTOR, '#pp-skapa__main-page-navigation-1 > button > '
                                               'span.pp-skapa__list-view-item__control-icon > svg > path')
    choose_store = (U.By.CSS_SELECTOR, '#root > div > main > div.grid_gridRight__NukI\+.preferred-store'
                                       '-page_wrapperRight__7S8Cn > button')
    stores_manu = (U.By.CSS_SELECTOR, '#selectStoreDropdown')
    rishon_le_zion_store = (U.By.CSS_SELECTOR, '#selectStoreDropdown > option:nth-child(5)')

    Delete_User_Password = (U.By.CSS_SELECTOR, '#password')

    Delete_User_Section = (U.By.CSS_SELECTOR, '#pp-skapa__main-page-navigation-3 > button > '
                                              'span.pp-skapa__list-view-item__control-icon > svg')
    Delete_User_Button = (U.By.CSS_SELECTOR, '#root > div > main > div.grid_gridLeft__0Kzru.delete-account'
                                             '-page_content__DPF2A > div:nth-child(9) > form > button')

    # Creating the personal area actions
    def click_on_my_profile(self):
        self.click(self.My_profile)

    def click_edit_personal_info_BTN(self):
        self.click(self.Edit_Personal_INFO_BTN)

    def insert_new_name(self):
        self.insert(self.Edit_first_name, 'Mark')

    def insert_new_last_name(self):
        self.insert(self.Edit_Last_name, 'Bryce')

    def insert_birth_year(self):
        self.insert(self.Edit_Birth_year, '1995')

    def insert_birth_month(self):
        self.insert(self.Edit_Birth_month, '02')

    def insert_birth_day(self):
        self.insert(self.Edit_Birth_Day, '25')

    def click_on_change_password_BTN(self):
        self.click(self.Change_password_BTN)

    def insert_current_password(self):
        self.insert(self.Current_Password, 'Mike123@')

    def insert_new_password(self):
        self.insert(self.Edit_New_Password, 'Galin123@')

    def confirm_new_password(self):
        self.insert(self.Confirm_New_Password, 'Galin123@')

    def click_on_save_new_password(self):
        self.click(self.Confrim_passsword_button)

    def click_on_save_BTN(self):
        self.click(self.SAVE_BTN)

    def click_on_preferred_store(self):
        self.click(self.Preferred_Ikea_store)

    def click_on_choose_store(self):
        self.click(self.choose_store)

    def choose_Rishon_Le_Zion_Store(self):
        self.click(self.rishon_le_zion_store)

    def is_personal_details_saved(self):
        pass

    def is_password_changed(self):
        pass

    def get_preferred_store_name(self):
        pass

    def click_on_delete_user_section(self):
        self.click(self.Delete_User_Section)

    def insert_valid_delete_user_password(self):
        self.insert(self.Delete_User_Password, 'Mikegold123@')

    def insert_invalid_delete_user_password(self):
        self.insert(self.Delete_User_Password, 'jkljjljll')

    def click_on_delete_account(self):
        self.click(self.Delete_User_Button)

    def is_account_deleted(self):
        pass

    def is_error_message_displayed(self):
        pass

