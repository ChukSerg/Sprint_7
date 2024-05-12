import allure
import requests

from utils.constants import ApiConstants


class ApiOrder:
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(order):
        return requests.post(ApiConstants.ORDER_URL, data=order)

    @staticmethod
    @allure.step('Получение списка заказов')
    def get_list_of_orders():
        return requests.get(ApiConstants.ORDER_URL)


