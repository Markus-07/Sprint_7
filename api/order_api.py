import requests

from data import BASE_URL, CREATE_ORDER, GET_ORDERS


def create_order(first_name, last_name, address, metro_station, phone,
                 rent_time, delivery_date, comment=None, color=None):
    payload = {
        "firstName": first_name,
        "lastName": last_name,
        "address": address,
        "metroStation": metro_station,
        "phone": phone,
        "rentTime": rent_time,
        "deliveryDate": delivery_date,
    }
    if comment is not None:
        payload["comment"] = comment
    if color is not None:
        payload["color"] = color
    return requests.post(f"{BASE_URL}{CREATE_ORDER}", json=payload)


def get_orders():
    return requests.get(f"{BASE_URL}{GET_ORDERS}")
