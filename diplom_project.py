import configuration
import requests
import data


def post_create_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body,
                         headers=data.headers)


response_new_order = post_create_new_order()
track = response_new_order.json()["track"]


def get_find_order():
    return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER + "?t=" + str(track))

# Кабиров Марат, 8-я когорта – Финальный проект. Инженер по тестированию Плюс


def test_response_code_is_200():
    assert get_find_order().status_code == 200, "Ожидался код 200, но получен {response.status_code}"
