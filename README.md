<<<<<<< HEAD
﻿# 🧪 API Tests — Yandex.Prilavok  
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
=======
#  API Tests — Yandex.Prilavok  

###  Описание  
Проект к Спринту 10 **тестирования API сервиса Яндекс.Прилавок** с использованием библиотеки **pytest**.  
Цель — автоматизировать чек-лист и сдать файлы с кодом в виде архива, проверить корректность работы метода **создания наборов пользователей** (`/api/v1/kits`) и связанных запросов API.

---

## Структура проекта  

| Файл | Назначение |
|------|-------------|
|  **settings.py** | Хранит базовый URL сервиса и пути (`/api/v1/users`, `/api/v1/kits`). |
|  **data.py** | Содержит шаблоны тел запросов и вспомогательные функции для подготовки данных. |
|  **sender_stand_request.py** | Функции для отправки HTTP-запросов (POST-запросы для создания пользователя и набора). |
|  **create_kit_name_kit_test.py** | Тесты Pytest для позитивных и негативных сценариев создания набора. |
|  **README.md** | Текущее описание проекта и инструкция по запуску тестов. |
|  **.gitignore** | Исключает служебные файлы и папки (`__pycache__`, `.venv`, `.vscode` и т.д.). |
---

###  Изменения в названии файлов  
В процессе выполнения проекта возникала ошибка при использовании имени файла **`configuration.py`** —  
интерпретатор Python не распознавал модуль корректно.  

Чтобы устранить проблему, файл был переименован в **`settings.py`**.  
Все импорты и ссылки на него были обновлены, после чего тесты успешно выполняются.  

---
>>>>>>> origin/main

---

##  Используемые технологии  

<<<<<<< HEAD
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
=======
- **Python** ≥ 3.13  
- **Pytest** ≥ 8.4  
- **Requests** (для работы с API)  

---

##  Запуск проекта  

### 1️⃣ Клонировать репозиторий:
```bash
git clone <ссылка-на-репозиторий>
cd yandex_api_stand_tests
```

### 2️⃣ Создать и активировать виртуальное окружение:
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Установить зависимости (если есть `requirements.txt`):
```bash
pip install -r requirements.txt
```

### 4️⃣ Запустить тесты:
```bash
pytest create_kit_name_kit_test.py -v
```

---

##  Описание тестов  

Проект включает тесты, реализованные на основе чек-листа:

### Позитивные проверки:
- Создание набора с корректным именем (1–511 символов);  
- Проверка допустимых символов (русские, латинские, цифры, пробелы, спецсимволы).

### Негативные проверки:
- Пустое значение `name`;  
- Имя длиннее 511 символов;  
- Некорректные символы.  

 Некоторые тесты **должны завершаться со статусом FAILED** — это соответствует требованиям чек-листа и заданию.

---

##  Пример запуска  

```bash
pytest create_kit_name_kit_test.py -v
```

**Результат:**
```
collected 9 items

create_kit_name_kit_test.py::test_name_len_1 PASSED
create_kit_name_kit_test.py::test_name_len_0 FAILED
create_kit_name_kit_test.py::test_name_len_511 PASSED
create_kit_name_kit_test.py::test_name_len_512 FAILED
create_kit_name_kit_test.py::test_name_english_letters PASSED
create_kit_name_kit_test.py::test_name_russian_letters PASSED
create_kit_name_kit_test.py::test_name_special_symbols PASSED
create_kit_name_kit_test.py::test_name_spaces_allowed PASSED
create_kit_name_kit_test.py::test_name_digits_allowed PASSED
```

---

##  Автор  

**Юлия Тюлюпа 37 кагорта**  
 Email: [yul5876@yandex.ru](mailto:yul5876@yandex.ru)
>>>>>>> origin/main
