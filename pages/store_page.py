import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import StorePageLocators


class StorePage(BasePage):
    def should_be_guest_can_add_item_to_cart(self):
        self.should_be_guest_can_accept_region_location()
        self.should_be_guest_can_accept_cookie()
        self.should_be_guest_can_mouse_over_group()
        self.should_be_guest_can_choose_group_store()
        time.sleep(7)
        # self.should_be_guest_can_close_popup_sale()
        self.should_be_guest_can_click_item_link()
        self.should_be_guest_can_choose_size()
        self.should_be_guest_can_click_button_add_to_cart()

    def should_be_guest_can_accept_region_location(self):
        if self.is_element_present(StorePageLocators.ACCEPT_LOCATION):
            self.browser.find_element(*StorePageLocators.ACCEPT_LOCATION).click()

    def should_be_guest_can_accept_cookie(self):
        time.sleep(1)
        self.browser.find_element(*StorePageLocators.ACCEPT_COOKIE).click()

    def should_be_guest_can_mouse_over_group(self):
        self.mouse_hover_element(StorePageLocators.SHOP_BY_TEAM)

    def should_be_guest_can_choose_group_store(self):
        self.browser.find_element(*StorePageLocators.BY_CONFERENCE).click()

    def should_be_guest_can_close_popup_sale(self):
        self.browser.find_element(*StorePageLocators.POPUP_SALE_CLOSE).click()

    def should_be_guest_can_click_item_link(self):
        self.browser.find_element(*StorePageLocators.STORE_ITEM).click()

    def should_be_guest_can_choose_size(self):
        self.browser.find_element(*StorePageLocators.SIZE_SELECTOR).click()

    def should_be_guest_can_click_button_add_to_cart(self):
        self.browser.find_element(*StorePageLocators.BUTTON_ADD_TO_CART).click()