from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_input_login(self, text):
        self.browser.find_element(*LoginPageLocators.LOGIN_FIELD).send_keys(text)

    def should_be_input_password(self, text):
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(text)

    def should_be_click_button_signin(self):
        self.browser.find_element(*LoginPageLocators.BUTTON_SIGN_IN).click()
