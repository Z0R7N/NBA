import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    # to check the presence of an element on the page
    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
        except (NoSuchElementException):
            return False
        return True

    def mouse_hover_element(self, locator):
        action = ActionChains(self.browser)
        element = self.browser.find_element(*locator)
        action.move_to_element(element).click().perform()

    # returning a value from the text of an element
    def find_price_item(self, locator):
        time.sleep(1)
        price = self.browser.find_element(*locator).text
        return price
