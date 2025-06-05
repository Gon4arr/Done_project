from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.send_keys((By.ID, "user-name"), username)
        self.send_keys((By.ID, "password"), password)
        self.click((By.ID, "login-button"))

    def get_error_message(self):
        try:
            error_element = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
            return error_element.text
        except NoSuchElementException:
            return ""

