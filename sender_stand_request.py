# sender_stand_request.py

import requests
import configuration
import data

# Функция для создания нового пользователя


def post_new_user(user_body):
    """
    Отправляет запрос на создание нового пользователя.
    Принимает user_body. Возвращает объект Response.
    """
    url = configuration.URL_SERVICE + configuration.CREATE_USER_PATH

    # Отправка запроса с телом пользователя
    return requests.post(url, json=user_body)


# Функция для создания набора
def post_new_client_kit(kit_body: dict, auth_token: str):
    """
    Отправляет запрос на создание личного набора для пользователя.
    Требует заголовок Authorization. Возвращает объект Response.
    """
    url = configuration.URL_SERVICE + configuration.CREATE_KIT_PATH

    # 1. Создаем копию заголовков из data.py (для Content-Type)
    current_headers = data.auth_headers.copy()

    # 2. Устанавливаем заголовок Authorization в формате Bearer
    current_headers["Authorization"] = f"Bearer {auth_token}"

    # Отправка запроса с телом набора и заголовками
    return requests.post(url, json=kit_body, headers=current_headers)
