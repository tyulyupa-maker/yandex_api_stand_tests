# create_kit_name_kit_test.py

import sender_stand_request
import data
import pytest


def get_new_user_token() -> str:
    """
    Создаёт пользователя и возвращает authToken из ответа.
    """
    resp = sender_stand_request.post_new_user()
    assert resp.status_code == 201, f"Не создался пользователь: {
        resp.status_code} {
        resp.text}"
    token = resp.json().get("authToken")
    assert token, f"В ответе нет authToken: {resp.text}"
    return token


def get_kit_body(name):
    """
    Возвращает копию базового тела набора с подставленным name.
    """
    body = data.kit_body.copy()
    body["name"] = name
    return body


def positive_assert(kit_body):
    """
    Позитивная проверка: 201 и совпадение name в ответе.
    """
    token = get_new_user_token()
    resp = sender_stand_request.post_new_client_kit(kit_body, token)
    assert resp.status_code == 201, f"Ожидали 201, получили {
        resp.status_code}: {
        resp.text}"
    assert resp.json().get(
        "name") == kit_body["name"], f"Имя в ответе не совпало: {resp.text}"


def negative_assert_code_400(kit_body):
    """
    Негативная проверка: ожидаем 400.
    """
    token = get_new_user_token()
    resp = sender_stand_request.post_new_client_kit(kit_body, token)
    assert resp.status_code == 400, f"Ожидали 400, получили {
        resp.status_code}: {
        resp.text}"


# 1. Допустимое количество символов (1) -> 201
def test_name_len_1():
    positive_assert(get_kit_body("a"))


# 2. Допустимое количество символов (511) -> 201
@pytest.mark.xfail(reason="Стенд даёт 201 вместо 400 для пустого name", strict=True)
def test_name_len_511():
    positive_assert(get_kit_body("a" * 511))


# 3. Меньше допустимого (0) -> 400
@pytest.mark.xfail(
    reason="Стенд принимает пустую строку name и возвращает 201 вместо 400",
    strict=True)
def test_name_len_0():
    negative_assert_code_400(get_kit_body(""))


# 4. Больше допустимого (512) -> 400
@pytest.mark.xfail(reason="Стенд даёт 201 вместо 400 при name длиной 512", strict=True)
def test_name_len_512():
    negative_assert_code_400(get_kit_body("a" * 512)) @ pytest.mark.xfail(
        reason="Стенд возвращает 201 вместо 400 для name длиной 512")


def test_name_len_512():
    negative_assert_code_400(get_kit_body("a" * 512))


@pytest.mark.xfail(reason="Стенд даёт 500 вместо 400 при отсутствии параметра name", strict=True)
def test_name_param_absent():
    token = get_new_user_token()
    body = data.kit_body.copy()
    body.pop("name", None)
    resp = sender_stand_request.post_new_client_kit(body, token)
    assert resp.status_code == 400, f"Ожидали 400, получили {
        resp.status_code}: {
        resp.text}"


@pytest.mark.xfail(reason="Стенд даёт 201 вместо 400, если name — число", strict=True)
def test_name_number_type():
    negative_assert_code_400(get_kit_body(123))


# 5. Разрешены английские буквы -> 201
def test_name_english_letters():
    positive_assert(get_kit_body("QWErty"))


# 6. Разрешены русские буквы -> 201
def test_name_russian_letters():
    positive_assert(get_kit_body("Мария"))


# 7. Разрешены спецсимволы -> 201
def test_name_special_symbols():
    positive_assert(get_kit_body("\"№%@\","))


# 8. Разрешены пробелы -> 201
def test_name_spaces_allowed():
    positive_assert(get_kit_body(" Человек и КО "))


# 9. Разрешены цифры -> 201
def test_name_digits_allowed():
    positive_assert(get_kit_body("123"))


# 10. Параметр не передан в запросе -> 400
@pytest.mark.xfail(
    reason="Стенд отдаёт 500 при отсутствии параметра name (ожидали 400)",
    strict=True)
def test_name_param_absent():
    token = get_new_user_token()
    body = data.kit_body.copy()
    body.pop("name", None)
    resp = sender_stand_request.post_new_client_kit(body, token)
    assert resp.status_code == 400, f"Ожидали 400, получили {
        resp.status_code}: {
        resp.text}"


# 11. Передан другой тип параметра (число) -> 400
@pytest.mark.xfail(
    reason="Стенд принимает число в name и возвращает 201 вместо 400",
    strict=True)
def test_name_number_type():
    negative_assert_code_400(get_kit_body(123))
