# create_kit_name_kit_test.py (ФИНАЛЬНАЯ ВЕРСИЯ)

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
    # Оптимизация: Если токен уже есть, возвращаем его
    if AUTH_TOKEN:
        return AUTH_TOKEN

    # Отправка запроса на создание пользователя, передаем тело
    # ПРИМЕЧАНИЕ: Предполагается, что post_new_user в sender_stand_request.py принимает data.user_body
    resp = sender_stand_request.post_new_user(data.user_body)

    assert resp.status_code == 201, f"Не создался пользователь: {resp.status_code} {resp.text}"

    token = resp.json().get("authToken")
    assert token, f"В ответе нет authToken: {resp.text}"

    # Сохраняем токен
    AUTH_TOKEN = token
    return token


def get_kit_body(name=None):
    """
    Возвращает копию базового тела набора.
    Если name=None, поле 'name' удаляется из тела (Случай #10).
    """
    # Создаем копию
    body = data.kit_body.copy()

    # Обработка Случая #10: Параметр не передан (name=None)
    if name is None:
        if 'name' in body:
            del body['name']
    # Все остальные случаи
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

    # Проверяем имя в ответе
    expected_name = kit_body.get("name")
    actual_name = resp.json().get("name")

    assert actual_name == expected_name, f"Имя в ответе не совпало. Ожидали: '{expected_name}', Получили: '{actual_name}'"


def negative_assert_code_400(kit_body):
    """
    Негативная проверка: ожидаем код 400.
    """
    token = get_new_user_token()
    resp = sender_stand_request.post_new_client_kit(kit_body, token)

    # Если стенд вернет 201 или 500, тест упадет (FAILED), что допустимо по заданию
    assert resp.status_code == 400, f"Ожидали 400, получили {resp.status_code}: {resp.text}"


# --------------------- Тесты ---------------------

# 1. Допустимое количество символов (1) -> 201
def test_name_len_1():
    positive_assert(get_kit_body(data.kit_name_1_char))

# 2. Допустимое количество символов (511) -> 201


def test_name_len_511():
    positive_assert(get_kit_body(data.kit_name_511_chars))

# 3. Меньше допустимого (0) -> 400


def test_name_len_0():
    negative_assert_code_400(get_kit_body(data.kit_name_0_chars))

# 4. Больше допустимого (512) -> 400


def test_name_len_512():
    negative_assert_code_400(get_kit_body(data.kit_name_512_chars))

# 5. Разрешены английские буквы -> 201


def test_name_english_letters():
    positive_assert(get_kit_body(data.kit_name_en_chars))

# 6. Разрешены русские буквы -> 201


def test_name_russian_letters():
    positive_assert(get_kit_body(data.kit_name_ru_chars))

# 7. Разрешены спецсимволы -> 201


def test_name_special_symbols():
    positive_assert(get_kit_body(data.kit_name_special_chars))

# 8. Разрешены пробелы -> 201


def test_name_spaces_allowed():
    positive_assert(get_kit_body(data.kit_name_with_spaces))

# 9. Разрешены цифры -> 201


def test_name_digits_allowed():
    positive_assert(get_kit_body(data.kit_name_digits))

# 10. Параметр не передан в запросе -> 400


def test_name_param_absent():
    negative_assert_code_400(get_kit_body(name=None))

# 11. Передан другой тип параметра (число) -> 400


def test_name_number_type():
    negative_assert_code_400(get_kit_body(data.kit_name_number_type))
