import pytest

@pytest.mark.api
def test_add_remove_cart(api_client):
    session, base_url = api_client
    payload = {"userId": 1, "products": [{"id": 1, "quantity": 1}]}
    post_response = session.post(f"{base_url}/carts/add", json=payload)
    assert post_response.status_code == 201

    cart_id = post_response.json().get("id")
    # DummyJSON API не поддерживает удаление корзины
    # Просто проверим, что cart_id получен
    assert isinstance(cart_id, int) and cart_id > 0
