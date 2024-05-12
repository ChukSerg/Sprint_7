import allure
import pytest

from api.couriers import ApiCourier
from utils.constants import ApiConstants


class TestCourierApi:
    @allure.title('Проверка регистрации курьера с валидными данными')
    def test_creation_courier_correct_data(self, create_static_courier):
        courier = create_static_courier
        response = ApiCourier.create_courier(courier[0], courier[1], courier[2])
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверка невозможности повторного создания курьера')
    def test_negative_creation_two_same_couriers(self, create_random_courier):
        courier = create_random_courier
        response = ApiCourier.create_courier(courier[0], courier[1], courier[2])
        assert (response.status_code == 409 and
                response.json()['message'] == ApiConstants.CREATE_TWO_SAME_MESSAGE)

    @allure.title('Проверка невозможности создания курьера с неполными данными')
    @pytest.mark.parametrize('data', [["", "password456", "TestName1"], ["login456", "", "TestName2"]])
    def test_negative_creation_without_data(self, data):
        response = ApiCourier.create_courier(*data)
        assert (response.status_code == 400 and
                response.json()['message'] == ApiConstants.LOST_CREATE_DATA_MESSAGE)

    @allure.title('Проверка успешного логина курьера')
    def test_login_courier_success(self, create_random_courier):
        courier = create_random_courier
        response = ApiCourier.login_courier(courier[0], courier[1])
        assert response.status_code == 200 and 'id' in response.json()

    @allure.title('Проверка невозможности логина курьера без указания пароля')
    def test_login_courier_lost_password(self, create_random_courier):
        courier = create_random_courier
        response = ApiCourier.login_courier(courier[0], '')
        assert response.status_code == 400 and response.json()['message'] == ApiConstants.LOST_LOGIN_DATA_MESSAGE

    @allure.title('Проверка невозможности логина курьера без указания логина')
    def test_login_courier_lost_login(self, create_random_courier):
        courier = create_random_courier
        response = ApiCourier.login_courier('', courier[1])
        assert response.status_code == 400 and response.json()['message'] == ApiConstants.LOST_LOGIN_DATA_MESSAGE

    @allure.title('Проверка невозможности логина курьера с неверным логином')
    def test_wrong_courier_login(self, create_random_courier):
        courier = create_random_courier
        response = ApiCourier.login_courier('testWrongLogin', courier[1])
        assert response.status_code == 404 and response.json()['message'] == ApiConstants.WRONG_LOGIN_DATA_MESSAGE

    @allure.title('Проверка невозможности логина курьера с неверным паролем')
    def test_wrong_courier_password(self, create_random_courier):
        courier = create_random_courier
        response = ApiCourier.login_courier(courier[0], 'testWrongPassword')
        assert response.status_code == 404 and response.json()['message'] == ApiConstants.WRONG_LOGIN_DATA_MESSAGE
