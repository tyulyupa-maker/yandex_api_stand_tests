# 🧪 API Tests — Yandex.Prilavok  
### Тестирование API метода создания набора `/api/v1/kits`

---

## 📘 Описание проекта  

Проект к **Спринту 10** по теме **тестирования API сервиса Яндекс.Прилавок**.  
Основная цель — автоматизировать чек-лист для метода **создания набора** (`POST /api/v1/kits`)  
и связанных запросов API с помощью **pytest** и **requests**.

---

## 🗂 Структура проекта  

| Файл | Назначение |
|------|-------------|
| **configuration.py** | Содержит базовый URL стенда (`URL_SERVICE`) и пути: `/api/v1/users`, `/api/v1/kits`. |
| **data.py** | Хранит шаблоны тел запросов (`user_body`, `kit_body`) и вспомогательные функции. |
| **sender_stand_request.py** | Выполняет HTTP-запросы: создание пользователя и набора. |
| **create_user_test.py** | Основные тесты Pytest по чек-листу (позитивные и негативные сценарии). |
| **pytest.ini** | (Необязательно) настройки Pytest, включая формат вывода и маркеры. |
| **requirements.txt** | (Необязательно) список зависимостей проекта. |
| **README.md** | Описание проекта и инструкция по запуску. |

> **Важно:**  
> Учебный стенд **динамический** — при его перезапуске URL меняется.  
> Всегда нужно обновлять перед запуском `URL_SERVICE` в `configuration.py` на актуальный адрес перед запуском тестов.

---

##  Используемые технологии  

- **Python** ≥ 3.10  
- **Pytest** ≥ 8.0  
- **Requests** ≥ 2.31  

---

## 💻 Подготовка окружения (Windows, PowerShell)

```bash
# 1️⃣ Создать и активировать виртуальное окружение
python -m venv .venv
.venv\Scripts\Activate.ps1

# 2️⃣ Установить зависимости
pip install -U pip
pip install pytest requests
# или (если есть requirements.txt)
pip install -r requirements.txt
🧩 Конфигурация проекта

Перед запуском тестов:

Открой файл configuration.py.

Проверь, что указаны актуальные значения:

URL_SERVICE = "https://<текущий-url-стенда>"
CREATE_USER_PATH = "/api/v1/users"
CREATE_KIT_PATH  = "/api/v1/kits"


Сохрани файл.

🚀 Запуск тестов

Из корня проекта:

# Активировать виртуальное окружение (если ещё не активировано)
.venv\Scripts\Activate.ps1

# Запуск всех тестов
python -m pytest -vv -rx


-vv — подробный вывод результатов;

-rx — показывает причины xfail (ожидаемых падений).

Для запуска только тестов создания набора:

python -m pytest create_user_test.py -vv -rx

✅ Чек-лист тестов

Проверяются сценарии для параметра name при создании набора.

Позитивные (ожидаемый код ответа 201)
№	Ввод	Описание
1	"a"	1 символ
2	511 символов	Верхняя граница допустимой длины
3	"QWErty"	Английские буквы
4	"Мария"	Русские буквы
5	"\"№%@\","	Спецсимволы
6	" Человек и КО "	Пробелы
7	"123"	Цифры
Негативные (ожидаемый код ответа 400)
№	Ввод	Комментарий
1	""	Пустая строка (xfail — стенд возвращает 201)
2	512 символов	Длина больше допустимой (xfail — стенд возвращает 201)
3	name не передан	(xfail — стенд возвращает 500)
4	name: 123 (число)	(xfail — стенд возвращает 201)

Тесты, помеченные xfail, — это известные расхождения учебного стенда со спецификацией,
они не считаются ошибками автотестов.

## 💻 Результат
collected 11 items

collected 11 items

create_user_test.py::test_name_len_1 PASSED
create_user_test.py::test_name_len_511 PASSED
create_user_test.py::test_name_len_0 XFAIL (Стенд принимает пустую строку name и возвращает 201 вместо 400)
create_user_test.py::test_name_len_512 XFAIL (Стенд принимает 512 символов и возвращает 201 вместо 400)
create_user_test.py::test_name_param_absent XFAIL (Стенд отдаёт 500 при отсутствии параметра name (ожидали 400))
create_user_test.py::test_name_number_type XFAIL (Стенд принимает число в name и возвращает 201 вместо 400)
create_user_test.py::test_name_english_letters PASSED
create_user_test.py::test_name_russian_letters PASSED
create_user_test.py::test_name_special_symbols PASSED
create_user_test.py::test_name_spaces_allowed PASSED
create_user_test.py::test_name_digits_allowed PASSED
                                                  

👩‍💻 Автор

Юлия Тюлюпа (37 кагорта)
📧 yul5876@yandex.ru
