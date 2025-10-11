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

---

##  Используемые технологии  

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
