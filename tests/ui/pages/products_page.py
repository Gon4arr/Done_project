from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductsPage(BasePage):
    products_title = (By.CLASS_NAME, "title")
    add_to_cart_buttons = (By.CSS_SELECTOR, "button.btn_inventory")
    shopping_cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def is_loaded(self):
        return self.find(self.products_title).text == "Products"

    def add_first_product_to_cart(self):
        buttons = self.driver.find_elements(*self.add_to_cart_buttons)
        if buttons:
            buttons[0].click()

    def open_cart(self):
        self.click(self.shopping_cart_link)
