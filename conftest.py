import pytest
import requests
from selenium import webdriver
import os

@pytest.fixture(scope="module")
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    for item in request.session.items:
        rep = getattr(item, "rep_call", None)
        if rep and rep.failed:
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            driver.save_screenshot(f"screenshots/{item.name}.png")
    driver.quit()

def pytest_runtest_makereport(item, call):
    if "driver" in item.fixturenames:
        if call.when == "call":
            setattr(item, "rep_call", call)

@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    # Базовый URL настоящего API для тестирования
    base_url = "https://dummyjson.com"
    yield session, base_url
    session.close()

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()