import time

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_be_click_link_account(self):
        self.browser.find_element(*MainPageLocators.SIGNIN_LINK).click()

    def should_be_click_link_enter_sign_in(self):
        self.browser.find_element(*MainPageLocators.ENTER_SIGN_LINK).click()

    # in Russia there is a redirect to another website address
    def should_be_correct_url(self):
        time.sleep(1)
        if self.is_element_present(MainPageLocators.NBA_LINK):
            self.browser.find_element(*MainPageLocators.NBA_LINK).click()

    def should_be_accept_cookie(self):
        if self.is_element_present(MainPageLocators.MESSAGE_ACCEPT):
            self.browser.find_element(*MainPageLocators.MESSAGE_ACCEPT).click()

    def should_be_element_is_visible(self):
        assert self.is_element_present(MainPageLocators.MENU_ACCOUNT), "authorisation is not success"

    def should_be_guest_can_click_link_games(self):
        self.browser.find_element(*MainPageLocators.GAMES_LINK).click()
