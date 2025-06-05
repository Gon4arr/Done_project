import pytest

@pytest.mark.api
def test_get_products(api_client):
    session, base_url = api_client
    response = session.get(f"{base_url}/products")
    assert response.status_code == 200
    data = response.json().get("products", [])
    assert isinstance(data, list)
    if data:
        assert "title" in data[0]
        assert "price" in data[0]
