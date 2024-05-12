import allure
import pytest

from api.orders import ApiOrder
from utils.constants import ApiConstants


class TestOrderApi:
    @allure.title('Проверка успешного создания заказа')
    def test_success_order_creation(self):
        response = ApiOrder.create_order(ApiConstants.DATA_ORDER_CREATION)
        assert response.status_code == 201 and 'track' in response.json()

    @allure.title('Проверка возможности заказа с выбором разных цветов')
    @pytest.mark.parametrize('color', [[], ['GREY', ''], ['BLACK', ''], ['BLACK', 'GREY']])
    def test_order_creation(self, color):
        payload = ApiConstants.DATA_ORDER_CREATION
        payload['color'] = color
        response = ApiOrder.create_order(payload)
        assert response.status_code == 201 and 'track' in response.json()

    @allure.title('Проверка, что в ответе возвращается список заказов')
    def test_return_list_of_orders(self):
        response = ApiOrder.get_list_of_orders()
        print(type(response.json()['orders']))
        assert response.status_code == 200 and isinstance(response.json()['orders'], list)

