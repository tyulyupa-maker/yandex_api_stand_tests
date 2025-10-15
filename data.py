# data.py
<<<<<<< HEAD
# Заголовки для JSON
headers = {
    "Content-Type": "application/json"
}

# Тело запроса на создание пользователя (для получения authToken)
user_body = {
    "firstName": "Мария",
    "phone": "+79990000000",
    "address": "Москва"
}

# Тело запроса на создание набора
kit_body = {
    "name": "Набор по умолчанию"
}

# Вспомогательная функция для токена авторизации


def make_auth_header(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}
=======

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
>>>>>>> origin/main
