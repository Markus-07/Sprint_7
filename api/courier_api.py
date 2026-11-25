import requests

from data import BASE_URL, CREATE_COURIER, LOGIN_COURIER, DELETE_COURIER


def create_courier(login, password, first_name):
    payload = {}
    if login is not None:
        payload["login"] = login
    if password is not None:
        payload["password"] = password
    if first_name is not None:
        payload["firstName"] = first_name

    return requests.post(f"{BASE_URL}{CREATE_COURIER}", json=payload)


def courier_login(login, password):
    payload = {}
    if login is not None:
        payload["login"] = login
    if password is not None:
        payload["password"] = password

    return requests.post(f"{BASE_URL}{LOGIN_COURIER}", json=payload)


def delete_courier(courier_id):
    return requests.delete(f"{BASE_URL}{DELETE_COURIER.format(courier_id)}")
    