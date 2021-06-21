from selenium.webdriver.common.by import By


class MainPageLocators():
    SIGNIN_LINK = (By.CSS_SELECTOR, "#nbaMenuButton")
    ENTER_SIGN_LINK = (By.CSS_SELECTOR, "#nbaMenuNBASignIn")
    NBA_LINK = (By.CSS_SELECTOR, "#global-nav-1 .nba-site a")
    MESSAGE_ACCEPT = (By.CSS_SELECTOR, "#onetrust-button-group #onetrust-accept-btn-handler")
    MENU_ACCOUNT = (By.CSS_SELECTOR, "#nbaMenuMyAccount")


class LoginPageLocators():
    LOGIN_FIELD = (By.CSS_SELECTOR, "#nbaLoginModalId")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#nbaLoginModalPw")
    BUTTON_SIGN_IN = (By.CSS_SELECTOR, "#nbaLoginModalSignIn")
    ACCOUNT_MANAGE = (By.CSS_SELECTOR, "#iptv_content")
