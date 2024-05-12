class ApiConstants:
    COURIER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    ORDER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    STATIC_COURIER = ['test_courier468', '123456', 'Test']
    CREATE_TWO_SAME_MESSAGE = 'Этот логин уже используется. Попробуйте другой.'
    LOST_CREATE_DATA_MESSAGE = 'Недостаточно данных для создания учетной записи'
    LOST_LOGIN_DATA_MESSAGE = 'Недостаточно данных для входа'
    WRONG_LOGIN_DATA_MESSAGE = 'Учетная запись не найдена'
    DATA_ORDER_CREATION = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["GREY", ""]
    }

