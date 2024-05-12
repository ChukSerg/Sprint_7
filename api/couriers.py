import requests
import allure

from utils.constants import ApiConstants


class ApiCourier:
    @staticmethod
    @allure.step('Регистрация нового курьера')
    def create_courier(login, password, first_name):
        url = ApiConstants.COURIER_URL
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return requests.post(url, data=payload)

    @staticmethod
    @allure.step('Логин курьера')
    def login_courier(login, password):
        url = f"{ApiConstants.COURIER_URL}/login"
        payload = {
            "login": login,
            "password": password
        }
        return requests.post(url, data=payload)

    @staticmethod
    @allure.step('Удаление курьера')
    def delete_courier(courier_id):
        url = f"{ApiConstants.COURIER_URL}/{courier_id}"
        return requests.delete(url)

    @staticmethod
    @allure.step('Получение id курьера')
    def get_courier_id(login, password):
        response = ApiCourier.login_courier(login, password)
        if response.status_code == 200:
            return response.json()['id']
        else:
            return 0
