# Автоматизация теста API — Яндекс Самокат

## Описание
Проект создан для автоматизации проверки API сервиса Яндекс Самокат.  
Тест проверяет создание нового заказа и получение информации о заказе по треку.

Шаги теста:
1. Отправить запрос на создание заказа.
2. Сохранить номер трека из ответа.
3. Отправить запрос на получение заказа по треку.
4. Проверить, что код ответа равен 200.

## Используемые технологии
- Python 3
- Pytest
- Requests
- Visual Studio Code

## Структура проекта
yandex_api_stand_tests/
│
├── configuration.py # Настройки и пути API
├── data.py # Тестовые данные
├── sender_stand_request.py # Функции для отправки запросов
├── create_and_get_order_test.py # Автотест
├── pytest.ini # Конфигурация Pytest
├── requirements.txt # Зависимости
└── README.md # Описание проекта

bash
Копировать код

## Установка и запуск
1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/<имя_пользователя>/yandex_api_stand_tests.git
   cd yandex_api_stand_tests
Установить зависимости:

bash
Копировать код
pip install -r requirements.txt
Запустить тест:

bash
Копировать код
pytest create_and_get_order_test.py -v
Пример результата
cpp
Копировать код
create_and_get_order_test.py::test_create_and_get_order_success PASSED [100%]
Создан заказ, track = 123456
Автор

Тюлюпа Юлия 37 кагорта
Проект выполнен в рамках диплома по курсу «Инженер по тестированию» в Яндекс.Практикуме.