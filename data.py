# data.py

# Пример тела запроса для создания нового пользователя
new_user_body = {
    "firstName": "Мария",
    "phone": "+79990000000",
    "address": "Москва, Тверская, 1"
}


kit_body = {
    "name": "Тестовый набор"
}

def make_auth_header(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}