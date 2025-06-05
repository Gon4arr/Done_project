# Автоматизация тестирования Swag Labs

## О проекте

Проект автоматизации тестирования веб-приложения [Swag Labs](https://www.saucedemo.com/) с использованием Python, Selenium, Pytest и Allure.

## Стек технологий

- Python 3.8+
- Selenium WebDriver
- Pytest
- Requests
- Allure

## Установка

1. Клонировать репозиторий:

```bash
git clone <твоя-ссылка-на-репозиторий>
cd swag_labs_test_project
```

2. Создать и активировать виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. Установить зависимости:

```bash
pip install -r requirements.txt
```

## Запуск тестов

- UI тесты:

```bash
pytest -m ui --alluredir=allure-results
allure serve allure-results
```

- API тесты:

```bash
pytest -m api --alluredir=allure-results
allure serve allure-results
```

## Структура проекта

```
tests/
 ├── ui/
 │    ├── pages/
 │    │    ├── base_page.py
 │    │    ├── login_page.py
 │    │    └── products_page.py
 │    ├── test_ui_login.py
 │    └── test_ui_cart.py
 └── api/
      ├── test_api_products.py
      └── test_api_cart.py
```