import pytest

from helpers.generate_data import register_new_courier_and_return_login_password
from api.courier_api import courier_login, delete_courier


@pytest.fixture
def registered_courier():
    data = register_new_courier_and_return_login_password()
    assert data, "Не удалось зарегистрировать курьера"

    login, password, first_name = data
    response = courier_login(login, password)
    assert response.status_code == 200, f"Курьер не смог залогиниться: {response.text}"
    courier_id = response.json().get("id")

    yield {"login": login, "password": password, "first_name": first_name, "id": courier_id}

    if courier_id:
        delete_courier(courier_id)
