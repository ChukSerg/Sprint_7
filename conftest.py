import pytest

from utils.constants import ApiConstants

from api.couriers import ApiCourier
from utils.helpers import register_new_courier_and_return_login_password


@pytest.fixture(scope='function')
def create_random_courier():
    login_pass = register_new_courier_and_return_login_password()
    yield login_pass
    ApiCourier.delete_courier(ApiCourier.get_courier_id(login_pass[0], login_pass[1]))


@pytest.fixture(scope='function')
def create_static_courier():
    login_pass = ApiConstants.STATIC_COURIER
    yield login_pass
    ApiCourier.delete_courier(ApiCourier.get_courier_id(login_pass[0], login_pass[1]))
