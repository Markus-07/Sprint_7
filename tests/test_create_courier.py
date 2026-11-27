import pytest
import random
import allure
from api.courier_api import create_courier, courier_login, delete_courier


class TestCreateCourier:
    @allure.title("Создание курьера — успешный сценарий")
    def test_create_courier_success(self):
        login = "test_user_create_ok"
        password = "1234"
        first_name = "Saske"

        response = create_courier(login, password, first_name)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

        login_response = courier_login(login, password)
        courier_id = login_response.json().get("id")
        if courier_id:
            delete_courier(courier_id)

    @allure.title("Создание курьера — повторный вызов возвращает ошибку")
    def test_create_courier_twice_returns_error(self):
        login = f"dup_{random.randint(1000, 9999)}"

        r1 = create_courier(login, "1234", "Name")
        assert r1.status_code == 201

        r2 = create_courier(login, "1234", "Name")
        assert r2.status_code == 409

    @allure.title("Создание курьера — отсутствует обязательное поле {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field(self, missing_field):
        login = f"user_{missing_field}_{random.randint(0, 1000)}"
        payload = {"login": login, "password": "1234", "firstName": "Name"}
        payload.pop(missing_field)

        resp = create_courier(
            payload.get("login"),
            payload.get("password"),
            payload.get("firstName")
        )
        assert resp.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in resp.json().get("message", "")
