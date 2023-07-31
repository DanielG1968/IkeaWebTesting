import os
import Assets.Pages.Utils as U
from Assets.Pages.Commons import Commons
import pyautogui


class MenuPage(Commons):
    Menu_BTN = (U.By.CSS_SELECTOR, 'body > div.hnf-header-hamburger.hnf-page-container > div > div > '
                                   'button.hnf-btn--menu-label-button')
    Inspirations_and_Ideas = (U.By.CSS_SELECTOR, 'body > aside > div.hnf-menu__container.hnf-menu__container--default '
                                                 '> nav.hnf-menu__nav > ul.hnf-menu__nav__aux > li:nth-child(1) > a')
    Inspirations_and_Ideas_Welcome_To_My_Home_BTN = (U.By.CSS_SELECTOR, '#\33 16680c0-819a-11eb-9f04-f1e03d809943'
                                                                        '-heading')
    Inspirations_and_Ideas_BedRoom = (U.By.CSS_SELECTOR, '#feed-pill-bedroom > span')

    Opening_Hours_btn = (U.By.CSS_SELECTOR, 'body > aside > div.hnf-menu__container.hnf-menu__container--default > '
                                            'nav.hnf-menu__nav > ul.hnf-menu__nav__aux > li:nth-child(2) > a')

    Custom_Services = (U.By.CSS_SELECTOR, 'body > aside > div.hnf-menu__container.hnf-menu__container--default > '
                                          'nav.hnf-menu__nav > ul.hnf-menu__nav__aux > li:nth-child(3) > a')

    Home_Safety = (U.By.CSS_SELECTOR, 'body > aside > div.hnf-menu__container.hnf-menu__container--default > '
                                      'nav.hnf-menu__nav > ul.hnf-menu__nav__aux > li:nth-child(4) > a')
    My_Account_BTN = (U.By.CSS_SELECTOR, 'body > aside > div.hnf-menu__container.hnf-menu__container--default > '
                                         'nav.hnf-menu__nav > ul.hnf-menu__nav__aux > li:nth-child(5) > a')
    Eat_In_Ikea = (U.By.CSS_SELECTOR, 'body > aside > div.hnf-menu__container.hnf-menu__container--default > '
                                      'nav.hnf-menu__nav > ul.hnf-menu__nav__aux > li:nth-child(7) > a')
    Bedroom_Product = (U.By.CSS_SELECTOR, '#f64d5f50-8198-11eb-9f04-f1e03d809943 > div > div > div.ofeed-organic-feed '
                                          '> div > div.ofeed-thumbnail-grid')

    # Actions

    def Click_On_Menu_BTN(self):
        self.click(self.Menu_BTN)

    def Product_is_visible(self):
        self.find(self.Bedroom_Product)

    def Click_On_Inspirations_and_ideas_Section(self):
        self.click(self.Inspirations_and_Ideas)

    def Click_On_Inspirations_And_Ideas_Bedroom(self):
        self.click(self.Inspirations_and_Ideas_BedRoom)

    def Click_On_Inspirations_And_Ideas_Welcome_To_my_Home(self):
        self.click(self.Inspirations_and_Ideas_Welcome_To_My_Home_BTN)

    def Click_On_Opening_Hours_BTN(self):
        self.click(self.Opening_Hours_btn)

    def Click_On_Custom_Services(self):
        self.click(self.Custom_Services)

    def Click_On_Home_Safety(self):
        self.click(self.Home_Safety)

    def Click_On_My_Account(self):
        self.click(self.My_Account_BTN)

    def Click_On_Eat_In_Ikea(self):
        self.click(self.Eat_In_Ikea)
