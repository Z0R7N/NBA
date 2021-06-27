from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainPage():
    def test_user_can_login_to_account(self, browser):
        link = "https://www.nba.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_correct_url()
        page.should_be_accept_cookie()
        page.should_be_click_link_account()
        page.should_be_click_link_enter_sign_in()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_input_login("test.tester70@yandex.ru")
        login_page.should_be_input_password("123456789aA")
        login_page.should_be_click_button_signin()
        page.should_be_element_is_visible()


# python -m pytest -v --tb=line tests/test_main_page.py
