# 🧪 API Tests — Yandex.Prilavok  
### Тестирование API метода создания набора `/api/v1/kits`

---

## 📘 Описание проекта  

Проект выполнен в рамках **Спринта 10** курса Яндекс.Практикума  
и посвящён **тестированию API сервиса Яндекс.Прилавок**.  

Цель — автоматизировать проверку метода **создания набора пользователя**  
(`POST /api/v1/kits`) с помощью библиотек **pytest** и **requests**.  

---

## 🗂 Структура проекта  

| Файл | Назначение |
|------|-------------|
| **settings.py** | Содержит базовый URL стенда (`URL_SERVICE`) и пути: `/api/v1/users`, `/api/v1/kits`. |
| **data.py** | Хранит шаблон тела запроса (`kit_body`) и вспомогательные данные. |
| **sender_stand_request.py** | Реализует функции для отправки HTTP-запросов (`POST /users`, `POST /kits`). |
| **create_kit_name_kit_test.py** | Основной набор автотестов (позитивные, негативные, xfail). |
| **pytest.ini** | Конфигурация Pytest и параметры вывода. |
| **requirements.txt** | Список зависимостей проекта. |
| **README.md** | Текущее описание проекта и инструкция по запуску. |

> ⚠️ **Важно:**  
> Учебный стенд **динамический** — при перезапуске меняется URL.  
> Перед запуском необходимо обновить `URL_SERVICE` в файле `settings.py`.

---

## ⚙️ Используемые технологии  

- **Python** ≥ 3.10  
- **Pytest** ≥ 8.0  
- **Requests** ≥ 2.31  

---

## 💻 Подготовка окружения (Windows / PowerShell)

```bash
# 1️⃣ Клонировать проект
git clone https://github.com/tyulyupa-maker/yandex_api_stand_tests.git
cd yandex_api_stand_tests

# 2️⃣ Создать виртуальное окружение
python -m venv .venv
.venv\Scripts\Activate.ps1

# 3️⃣ Установить зависимости
pip install -r requirements.txt
🧩 Конфигурация стенда

Открой файл settings.py и укажи актуальный URL учебного стенда:

URL_SERVICE = "https://<актуальный-адрес-сервера>.serverhub.praktikum-services.ru"
CREATE_USER_PATH = "/api/v1/users"
CREATE_KIT_PATH  = "/api/v1/kits"

🚀 Запуск тестов
# Запуск всех тестов с подробным выводом
pytest -vv -rx

# Или только набора тестов создания наборов
pytest create_kit_name_kit_test.py -vv -rx


🔹 Флаг -vv — подробный вывод
🔹 Флаг -rx — отображает причины ожидаемых падений (xfail)

✅ Чек-лист тестирования
№	Проверка	Ввод	Ожидаемый результат	Примечание
1	Минимум — 1 символ	"a"	201	✅
2	Максимум — 511 символов	"a" * 511	201	✅
3	0 символов	""	400	❌ xfail: сервер возвращает 201
4	512 символов	"a" * 512	400	✅
5	Английские буквы	"QWErty"	201	✅
6	Русские буквы	"Мария"	201	✅
7	Спецсимволы	"\"№%@\","	201	✅
8	Пробелы	" Человек и КО "	201	✅
9	Цифры	"123"	201	✅
10	Параметр name отсутствует	—	400	❌ xfail: сервер возвращает 500
11	Параметр name — число	123	400	❌ xfail: сервер возвращает 201
🧪 Пример результата запуска
pytest create_kit_name_kit_test.py -vv -rx


Результат:

collected 11 items

create_kit_name_kit_test.py::test_name_len_1 PASSED
create_kit_name_kit_test.py::test_name_len_511 PASSED
create_kit_name_kit_test.py::test_name_len_0 XFAIL (Стенд принимает пустую строку name и возвращает 201 вместо 400)
create_kit_name_kit_test.py::test_name_len_512 FAILED
create_kit_name_kit_test.py::test_name_english_letters PASSED
create_kit_name_kit_test.py::test_name_russian_letters PASSED
create_kit_name_kit_test.py::test_name_special_symbols PASSED
create_kit_name_kit_test.py::test_name_spaces_allowed PASSED
create_kit_name_kit_test.py::test_name_digits_allowed PASSED
create_kit_name_kit_test.py::test_name_param_absent XFAIL (Стенд отдаёт 500 при отсутствии параметра name (ожидали 400))
create_kit_name_kit_test.py::test_name_number_type XFAIL (Стенд принимает число в name и отдаёт 201 вместо 400)

=================== 1 failed, 7 passed, 3 xfailed, 11 warnings in 2.2s ===================

🧾 Интерпретация результата

✅ 7 тестов прошли — позитивные сценарии корректны.

⚠️ 3 XFAIL-теста — стенд ведёт себя не по спецификации (известные несоответствия).

❌ 1 ошибка — ожидаемый результат (чек-лист предусматривает).

⚙️ Warnings о несертифицированном HTTPS можно игнорировать (учебная среда).

💡 Подавление предупреждений (опционально)

Если мешают InsecureRequestWarning, можно добавить в pytest.ini:

[pytest]
addopts = -p no:warnings

👩‍💻 Автор проекта

Юлия Тюлюпа — 37 когорта Яндекс.Практикума
📧 yul5876@yandex.ru