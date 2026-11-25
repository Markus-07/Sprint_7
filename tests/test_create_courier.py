import pytest
import random
from api.courier_api import create_courier, courier_login, delete_courier


class TestCreateCourier:

    def test_create_courier_success(self):
        payload = {
            "login": "test_user_create_ok",
            "password": "1234",
            "firstName": "Saske"
        }
        response = create_courier(payload["login"], payload["password"], payload["firstName"])
        assert response.status_code == 201
        assert response.json() == {"ok": True}

        login_response = courier_login(payload["login"], payload["password"])
        courier_id = login_response.json().get("id")
        if courier_id:
            delete_courier(courier_id)

    def test_create_courier_twice_returns_error(self):
        login = f"dup_{random.randint(1000, 9999)}"
        r1 = create_courier(login, "1234", "Name")
        assert r1.status_code == 201

        r2 = create_courier(login, "1234", "Name")
        assert r2.status_code == 409

    @pytest.mark.parametrize("missing_field", ["login", "password"])  # было: + "firstName"
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
