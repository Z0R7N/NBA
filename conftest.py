import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# function for choosing browser google chrome or firefox
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')


# function to launch selected browser with url and close browser after done work
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = Options()
        browser = webdriver.Chrome(options=options)
    else:
        fp = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    time.sleep(4)
    browser.quit()
