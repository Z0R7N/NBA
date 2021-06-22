from pages.base_page import BasePage
from pages.locators import StorePageLocators


class StorePage(BasePage):
    def should_be_guest_can_add_item_to_cart(self):
        self.should_be_guest_can_accept_region_location()
        self.should_be_guest_can_click_item_link()

    def should_be_guest_can_accept_region_location(self):
        self.browser.find_element(*StorePageLocators.ACCEPT_LOCATION).click()

    def should_be_guest_can_accept_cookie(self):
        self.browser.find_element(*StorePageLocators.ACCEPT_COOKIE).click()

    def should_be_guest_can_choose_group_store(self):
        self.browser.find_element(*StorePageLocators.SHOP_BY_TEAM).click()

    def should_be_guest_can_click_item_link(self):
        pass