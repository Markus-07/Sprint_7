import pytest
import allure
from api.order_api import create_order


class TestCreateOrder:
    @allure.title("Создание заказа — проверка вариантов цвета")
    @pytest.mark.parametrize(
        "color",
        [
            pytest.param(["BLACK"], id="black"),
            pytest.param(["GREY"], id="grey"),
            pytest.param(["BLACK", "GREY"], id="both"),
            pytest.param([], id="empty"),
        ]
    )
    def test_create_order_with_color_variants(self, color):
        response = create_order(
            first_name="Naruto",
            last_name="Uchiha",
            address="Konoha, 142 apt.",
            metro_station=4,
            phone="+7 800 355 35 35",
            rent_time=5,
            delivery_date="2026-06-06",
            comment="Saske, come back to Konoha",
            color=color
        )
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа — без поля color")
    def test_create_order_without_color_field(self):
        response = create_order(
            first_name="Naruto",
            last_name="Uchiha",
            address="Konoha, 142 apt.",
            metro_station=4,
            phone="+7 800 355 35 35",
            rent_time=5,
            delivery_date="2026-06-06",
            comment="Saske, come back to Konoha",
        )
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа — в ответе есть трек-номер")
    def test_create_order_body_has_track_number(self):
        response = create_order(
            first_name="Naruto",
            last_name="Uchiha",
            address="Konoha, 142 apt.",
            metro_station=4,
            phone="+7 800 355 35 35",
            rent_time=5,
            delivery_date="2026-06-06",
            comment="Saske, come back to Konoha",
        )
        assert response.status_code == 201
        assert response.json().get("track") is not None
