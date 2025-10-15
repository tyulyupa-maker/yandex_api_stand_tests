# sender_stand_request.py
import requests
import configuration
import data


def post_new_user():
    """
    Создаёт нового пользователя. Возвращает объект Response.
    """
    url = configuration.URL_SERVICE + configuration.CREATE_USER_PATH
    return requests.post(url, json=data.user_body)


def post_new_client_kit(kit_body, auth_token: str):
    """
    Создаёт набор (kit) для пользователя. Требуется токен.
    Возвращает объект Response.
    """
    url = configuration.URL_SERVICE + configuration.CREATE_KIT_PATH
    headers = {"Authorization": f"Bearer {auth_token}"}
    return requests.post(url, json=kit_body, headers=headers)
