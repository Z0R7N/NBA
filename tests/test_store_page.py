from pages.store_page import StorePage


class TestStorePage():
    def test_guest_can_add_item_to_cart(self, browser):
        link = "https://www.nbastore.eu/"
        store_page = StorePage(browser, link)
        store_page.open()
        store_page.should_be_guest_can_add_item_to_cart()

# python -m pytest -v --tb=line tests/test_store_page.py
