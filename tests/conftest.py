import pytest

from helpers.generate_data import generate_random_string
from api.courier_api import create_courier, courier_login, delete_courier


@pytest.fixture
def registered_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    response = create_courier(login, password, first_name)
    # если создание не сработает, тест просто упадёт с FAIL — это нормально

    login_response = courier_login(login, password)
    courier_id = login_response.json().get("id")

    yield {
        "login": login,
        "password": password,
        "first_name": first_name,
        "id": courier_id,
    }

    if courier_id:
        delete_courier(courier_id)
