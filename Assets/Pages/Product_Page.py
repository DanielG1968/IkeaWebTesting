import os
import Assets.Pages.Utils as U
from Assets.Pages.Commons import Commons
import pyautogui


class ProductPage(Commons):
    Product_Section = (U.By.CSS_SELECTOR, 'body > div.hnf-page-container.hnf-2nd-line'
                                          ' > div > div > nav > ul > li:nth-child(1) > a')
    Kids_And_Babies_Section = (U.By.CSS_SELECTOR, 'body > aside > div.hnf-menu__container.hnf-menu__container--default '
                                                  '> nav:nth-child(2) > ul > li:nth-child(15) > a')

    Kids_Section = (U.By.CSS_SELECTOR, 'body > aside > div.hnf-menu__container.hnf-menu__container--default > '
                                       'nav.hnf-menu__nav2.hnf-menu--active > ul > li:nth-child(15) > nav >'
                                       ' ul > li:nth-child(3) > a')
    Filter_Btn = (U.By.CSS_SELECTOR, 'body > main > div > div > div.plp-main-container > div.js-product-list > div > '
                                     'div.plp-filter.plp-clearfix > div.plp-filter-bar > div > button:nth-child(1)')
    Filter_Low_To_High_Price = (U.By.CSS_SELECTOR, 'body > main > div > div > div.plp-main-container >'
                                                   ' div.js-product-list > '
                                                   'div > div.plp-filter.plp-clearfix >'
                                                   ' div.plp-filter-bar > div:nth-child(4) > div > fieldset'
                                                   ' > label:nth-child(3) > span.plp-radio.plp-radio--subtle >'
                                                   ' input[type=radio]')
    Category_Button = (U.By.CSS_SELECTOR, 'body > main > div > div > div.plp-main-container > div.js-product-list > '
                                          'div > div.plp-filter.plp-clearfix > div.plp-filter-bar > div > '
                                          'button:nth-child(2)')
    Toys_For_Kids_Option = (U.By.CSS_SELECTOR, '#filter-CATEGORIES > '
                                               'label.plp-checkbox__wrapper.plp-checkbox__wrapper--18734 > '
                                               'span.plp-checkbox--subtle.plp-checkbox > span')

    Accepting_massage = (U.By.CSS_SELECTOR, '#onetrust-accept-btn-handler')

    Filter_Color = (U.By.CSS_SELECTOR, 'body > main > div > div > div.plp-main-container > div.js-product-list > div '
                                       '> div.plp-filter.plp-clearfix > div.plp-filter-bar > div > button:nth-child(5)')

    Green_color_btn = (U.By.CSS_SELECTOR, '#ירוק')

    New_Product_section = (U.By.CSS_SELECTOR, 'body > div.hnf-page-container.hnf-2nd-line > div > div > nav > ul > '
                                              'li:nth-child(3) > a')

    Avsteg_product = (U.By.CSS_SELECTOR, 'body > main > div > div > div.plp-main-container > div.js-product-list > '
                                         'div > div.plp-product-list > div > div:nth-child(3) > '
                                         'div.plp-product-list__fragment > div > div > div > a > div > '
                                         'div.pip-compact-price-package__additional-info > h3 > div > div > '
                                         'span.pip-header-section__title--small.notranslate')
    Rooms_Section = (U.By.CSS_SELECTOR, 'body > div.hnf-page-container.hnf-2nd-line > div > div > nav > ul > '
                                        'li:nth-child(2) > a')
    Bedroom_BTN = (U.By.CSS_SELECTOR, 'body > aside > div.hnf-menu__container.hnf-menu__container--default > '
                                      'nav:nth-child(3) > ul > li:nth-child(1) > a > span.mr__nav__title')

    # Product page actions:

    def Click_On_Products_Section(self):
        self.click(self.Product_Section)

    def Click_On_Kids_And_Babies_Section(self):
        self.click(self.Kids_And_Babies_Section)

    def Click_On_Kids_Section(self):
        self.click(self.Kids_Section)

    def Click_On_Filter_Button(self):
        self.click(self.Filter_Btn)

    def Click_On_Low_To_High_Price(self):
        self.click(self.Filter_Low_To_High_Price)

    def Click_On_Category_Button(self):
        self.click(self.Category_Button)

    def Click_On_Toys_For_Kids_Option(self):
        self.click(self.Toys_For_Kids_Option)

    def Click_On_Accept_Handler_MSG(self):
        self.click(self.Accepting_massage)

    def Click_On_Color_filter_Btn(self):
        self.click(self.Filter_Color)

    def Click_On_Green(self):
        self.click(self.Green_color_btn)

    def Click_On_New_Products(self):
        self.click(self.New_Product_section)

    def Click_On_Avsteg(self):
        self.click(self.Avsteg_product)

    def CLick_On_Rooms(self):
        self.click(self.Rooms_Section)

    def Click_On_Bedrooms(self):
        self.click(self.Bedroom_BTN)

    def is_kids_section_displayed(self):
        pass

    def are_products_sorted_low_to_high(self):
        pass

    def is_AVSTEG_displayed(self):
        pass

    def get_displayed_products(self):
        pass
