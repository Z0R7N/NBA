from pages.locators import StorePageLocators
from pages.store_page import StorePage


class TestStorePage():
    def test_guest_can_add_item_to_cart(self, browser):
        link = "https://www.nbastore.eu/"
        store_page = StorePage(browser, link)
        store_page.open()
        store_page.should_be_guest_can_add_item_to_cart()
        price_item = store_page.find_price_item(StorePageLocators.ITEM_PRICE)
        print(f"price item = {price_item}")
        store_page.should_be_guest_can_click_button_add_to_cart()
        price_cart = store_page.find_price_item(StorePageLocators.CART_PRICE)
        print(f"price cart = {price_cart}")
        store_page.should_be_price_is_equal(price_cart, price_item)


# python -m pytest -v --tb=line tests/test_store_page.py
# python -m pytest -v -s tests/test_store_page.py
