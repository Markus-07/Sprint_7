from api.order_api import get_orders
import pytest


class TestOrdersList:

    @pytest.mark.skip("Стенд возвращает 504, пока пропускаем")
    def test_get_orders_returns_list(self):
        response = get_orders()
        assert response.status_code == 200
        body = response.json()
        assert "orders" in body
        assert isinstance(body["orders"], list)
