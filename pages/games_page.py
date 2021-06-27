from pages.base_page import BasePage
from pages.locators import GamesPageLocators


class GamesPage(BasePage):
    def should_be_guest_can_close_popup(self):
        if self.is_element_present(GamesPageLocators.CLOSE_POPUP_WINDOW):
            self.browser.find_element(*GamesPageLocators.CLOSE_POPUP_WINDOW).click()

    def should_be_guest_can_click_calendar(self):
        self.browser.find_element(*GamesPageLocators.CALENDAR_DROPDOWN).click()

    def should_be_guest_can_choose_date(self):
        calendar = self.browser.find_elements(*GamesPageLocators.DATE_CALENDAR)
        for element in calendar:
            if self.element_has_games(element):
                element.click()
                break

    def element_has_games(self, element):
        if not element.get_attribute("disabled"):
            games = element.get_attribute("data-text")
            if games != "0 Games":
                return True
        return False

    def should_be_element_is_visible(self):
        assert self.browser.find_element(*GamesPageLocators.LINK_SCORE), "there is no link for SCORE or there is no games"