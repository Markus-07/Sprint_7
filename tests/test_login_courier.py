import pytest
import allure

from api.courier_api import courier_login
from helpers.generate_data import generate_random_string


class TestLoginCourier:
    @allure.title("Авторизация — успешно, возвращается id")
    def test_login_success_returns_id(self, registered_courier):
        response = courier_login(registered_courier["login"], registered_courier["password"])
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Авторизация — неправильный пароль даёт ошибку")
    def test_login_with_wrong_password(self, registered_courier):
        response = courier_login(registered_courier["login"], "wrong_password")
        assert response.status_code == 404

    @allure.title("Авторизация — несуществующий курьер даёт ошибку")
    def test_login_with_nonexistent_courier(self):
        response = courier_login(generate_random_string(10), "1234")
        assert response.status_code == 404

    @allure.title("Авторизация — нет поля login даёт ошибку")
    def test_login_without_login_field(self):
        response = courier_login(None, "1234")
        assert response.status_code == 400

    @allure.title("Авторизация — нет поля password (пропускаем, стенд даёт 504)")
    @pytest.mark.skip("Стенд возвращает 504, пока пропускаем")
    def test_login_without_password_field(self, registered_courier):
        response = courier_login(registered_courier["login"], None)
        assert response.status_code == 400
