import pytest
from tests.ui.pages.products_page import ProductsPage
from tests.ui.pages.login_page import LoginPage

@pytest.mark.ui
def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    products_page = ProductsPage(driver)
    products_page.add_first_product_to_cart()
    products_page.open_cart()
    assert "Your Cart" in driver.page_source

