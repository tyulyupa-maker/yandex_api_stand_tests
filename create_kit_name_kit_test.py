# create_kit_name_kit_test.py

import pytest
import sender_stand_request
import data
import copy


# Глобальная переменная для хранения токена
AUTH_TOKEN = None


# --- Вспомогательные функции ---

def get_new_user_token() -> str:
    """
    Создаёт пользователя (если токен не получен) и возвращает authToken.
    """
    global AUTH_TOKEN

    if AUTH_TOKEN:
        return AUTH_TOKEN

    # Создание пользователя
    resp = sender_stand_request.post_new_user(data.user_body)

    # Проверка успешного создания
    assert resp.status_code == 201, f"Не создался пользователь: {resp.status_code} {resp.text}"

    token = resp.json().get("authToken")
    assert token, f"В ответе нет authToken: {resp.text}"

    AUTH_TOKEN = token
    return token


def get_kit_body(name=None):
    """
    Возвращает копию базового тела набора.
    Если name = None, поле 'name' удаляется из тела (случай #10).
    """
    body = data.kit_body.copy()

    if name is None:
        body.pop('name', None)
    else:
        body['name'] = name

    return body


def positive_assert(kit_body):
    """
    Позитивная проверка: ожидаем код 201 и совпадение name в ответе.
    """
    token = get_new_user_token()
    resp = sender_stand_request.post_new_client_kit(kit_body, token)

    assert resp.status_code == 201, f"Ожидали 201, получили {resp.status_code}: {resp.text}"

    expected_name = kit_body.get("name")
    actual_name = resp.json().get("name")

    assert actual_name == expected_name, (
        f"Имя в ответе не совпало. Ожидали: '{expected_name}', Получили: '{actual_name}'"
    )


def negative_assert_code_400(kit_body):
    """
    Негативная проверка: ожидаем код 400.
    Если сервер возвращает 201 или 500 — тест должен упасть.
    """
    token = get_new_user_token()
    resp = sender_stand_request.post_new_client_kit(kit_body, token)

    assert resp.status_code == 400, (
        f"Ожидали 400, получили {resp.status_code}. "
        f"Ответ сервера: {resp.text}"
    )


# --------------------- Тесты ---------------------

def test_name_len_1():
    positive_assert(get_kit_body(data.kit_name_1_char))


def test_name_len_511():
    positive_assert(get_kit_body(data.kit_name_511_chars))


def test_name_len_0():
    negative_assert_code_400(get_kit_body(data.kit_name_0_chars))


def test_name_len_512():
    negative_assert_code_400(get_kit_body(data.kit_name_512_chars))


def test_name_english_letters():
    positive_assert(get_kit_body(data.kit_name_en_chars))


def test_name_russian_letters():
    positive_assert(get_kit_body(data.kit_name_ru_chars))


def test_name_special_symbols():
    positive_assert(get_kit_body(data.kit_name_special_chars))


def test_name_spaces_allowed():
    positive_assert(get_kit_body(data.kit_name_with_spaces))


def test_name_digits_allowed():
    positive_assert(get_kit_body(data.kit_name_digits))


def test_name_param_absent():
    negative_assert_code_400(get_kit_body(name=None))


def test_name_number_type():
    negative_assert_code_400(get_kit_body(data.kit_name_number_type))
