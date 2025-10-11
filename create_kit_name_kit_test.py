# create_kit_name_kit_test.py
import pytest
from sender_stand_request import post_new_user, post_new_client_kit
import data

def get_new_user_token() -> str:
    resp = post_new_user()
    assert resp.status_code == 201, f"Не создался пользователь: {resp.status_code} {resp.text}"
    token = resp.json().get("authToken")
    assert token, f"В ответе нет authToken: {resp.text}"
    return token

def get_kit_body(name):
    body = data.kit_body.copy()   
    body["name"] = name
    return body

def positive_assert(kit_body: dict):
    token = get_new_user_token()
    resp = post_new_client_kit(kit_body, token)
    assert resp.status_code == 201, f"Ожидали 201, получили {resp.status_code}: {resp.text}"
    assert resp.json().get("name") == kit_body["name"], f"Имя не совпало: {resp.json()}"

def negative_assert_code_400(kit_body: dict):
    token = get_new_user_token()
    resp = post_new_client_kit(kit_body, token)
    assert resp.status_code == 400, f"Ожидали 400, получили {resp.status_code}: {resp.text}"

# ===== тесты по чек-листу =====
def test_name_len_1():
    positive_assert(get_kit_body("a"))

def test_name_len_511():
    positive_assert(get_kit_body("a" * 511))

def test_name_len_0():
    negative_assert_code_400(get_kit_body(""))

def test_name_len_512():
    negative_assert_code_400(get_kit_body("a" * 512))

def test_name_english_letters():
    positive_assert(get_kit_body("QWErty"))

def test_name_russian_letters():
    positive_assert(get_kit_body("Мария"))

def test_name_special_symbols():
    positive_assert(get_kit_body("\"№%@\","))

def test_name_spaces_allowed():
    positive_assert(get_kit_body(" Человек и КО "))

def test_name_digits_allowed():
    positive_assert(get_kit_body("123"))