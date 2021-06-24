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


class StorePageLocators():
    ACCEPT_LOCATION = (By.CSS_SELECTOR, ".modal-content .responsive-image img")
    ACCEPT_COOKIE = (By.CSS_SELECTOR, ".cookie-consent-container-v2 .cookie-accept-button")
    SHOP_BY_TEAM = (By.CSS_SELECTOR, ".top-nav-item-link")
    BY_CONFERENCE = (By.CSS_SELECTOR, ".dropdown-column .dropdown-link-text")
    POPUP_SALE_CLOSE = (By.CSS_SELECTOR, ".modal-close-button")
    STORE_ITEM = (By.CSS_SELECTOR, ".product-image")
    SIZE_SELECTOR = (By.CSS_SELECTOR, ".size-selector-button")
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".button.large.primary")
    ITEM_PRICE = (By.CSS_SELECTOR, ".layout-row.pdp-price .money-value")
    CART_PRICE = (By.CSS_SELECTOR, ".shipping-val")