import pytest
import requests

@pytest.fixture(scope="module")
def api_client():
    session = requests.Session()
    base_url = "https://fakestoreapi.com"
    yield session, base_url
    session.close()
