# sender_stand_request.py
<<<<<<< HEAD
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
=======

import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
import settings as configuration
import data

urllib3.disable_warnings(InsecureRequestWarning)

session = requests.Session()
session.verify = False  #
session.timeout = 15

def post_new_user():
    """Создаёт пользователя и возвращает ответ (Response)."""
    url = configuration.URL_SERVICE + configuration.CREATE_USER_PATH
    return session.post(url, json=data.new_user_body)

def post_new_client_kit(kit_body: dict, auth_token: str):
    """Создаёт личный набор пользователя. Требуется токен Authorization."""
    url = configuration.URL_SERVICE + configuration.CREATE_KIT_PATH
    headers = data.make_auth_header(auth_token)
    return session.post(url, json=kit_body, headers=headers)
>>>>>>> origin/main
