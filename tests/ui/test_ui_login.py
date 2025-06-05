import pytest
from tests.ui.pages.login_page import LoginPage
from tests.ui.pages.products_page import ProductsPage

@pytest.mark.ui
@pytest.mark.parametrize("username,password,is_valid", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
])
def test_login(driver, username, password, is_valid):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    if is_valid:
        products_page = ProductsPage(driver)
        assert products_page.is_loaded()
    else:
        error_message = login_page.get_error_message()
        assert "Epic sadface" in error_message
