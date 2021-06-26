from pages.main_page import MainPage


class TestGamePage():
    def test_guest_can_choose_game(self, browser):
        link = "https://www.nba.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_correct_url()
        page.should_be_accept_cookie()

# python -m pytest -v --tb=line tests/test_game_page.py
# python -m pytest -v -s tests/test_game_page.py