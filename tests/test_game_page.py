from pages.games_page import GamesPage
from pages.main_page import MainPage


class TestGamePage():
    def test_guest_can_choose_game(self, browser):
        link = "https://www.nba.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_correct_url()
        page.should_be_accept_cookie()
        page.should_be_guest_can_click_link_games()
        games_page = GamesPage(browser, browser.current_url)
        games_page.should_be_guest_can_close_popup()
        games_page.should_be_guest_can_click_calendar()
        games_page.should_be_guest_can_choose_date()
        games_page.should_be_element_is_visible()


# python -m pytest -v --tb=line tests/test_game_page.py
# python -m pytest -v -s tests/test_game_page.py