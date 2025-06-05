import pytest

@pytest.mark.api
def test_add_cart_invalid_payload(api_client):
    session, base_url = api_client
    payload = {"wrongKey": "value"}
    response = session.post(f"{base_url}/carts/add", json=payload)
    # dummyjson вернёт 400 или 422 для неправильного payload
    assert response.status_code in [400, 422]
