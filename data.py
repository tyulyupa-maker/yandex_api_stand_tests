# data.py

# --- 1. Данные для создания пользователя (для получения authToken) ---
user_body = {
    "firstName": "Мария",
    "phone": "+79995553311",
    "address": "г. Москва, ул. Пушкина, д. 5"
}

# --- 2. Заголовок для авторизации (используется в sender_stand_request.py) ---
auth_headers = {
    "Content-Type": "application/json",
    "Authorization": ""  # Токен будет добавлен здесь в коде
}

# --- 3. Базовое тело запроса для создания набора (шаблон) ---
kit_body = {
    "name": "Набор"  # Имя будет заменено в тестах
}

# --- 4. Тестовые значения для проверок поля "name" из чек-листа ---

# №1. Допустимое количество символов (1)
kit_name_1_char = "a"

# №2. Допустимое количество символов (511)
kit_name_511_chars = (
    "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
)

# №3. Количество символов меньше допустимого (0)
kit_name_0_chars = ""

# №4. Количество символов больше допустимого (512)
kit_name_512_chars = (
    "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
)

# №5. Разрешены английские буквы
kit_name_en_chars = "QWErty"

# №6. Разрешены русские буквы
kit_name_ru_chars = "Мария"

# №7. Разрешены спецсимволы
kit_name_special_chars = "\"№%@\","

# №8. Разрешены пробелы
kit_name_with_spaces = " Человек и КО "

# №9. Разрешены цифры
kit_name_digits = "123"

# №11. Передан другой тип параметра (число)
kit_name_number_type = 123
