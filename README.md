# deathwave

Современный игровой портал для сообщества Minecraft с функциями форума, профилей пользователей и системой авторизации.

## Функциональность

- Регистрация и авторизация пользователей
- Профили пользователей с аватарами
- Форум с разделами и темами
- Система рейтинга и репутации
- Модерация контента
- Поиск по форуму

## Установка

1. Клонируйте репозиторий
2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate  # для Windows
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Примените миграции:
```bash
python manage.py migrate
```
5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```
6. Запустите сервер:
```bash
python manage.py runserver
```

## Технологии

- Django 5.0
- Bootstrap 5
- SQLite (для разработки)
- PostgreSQL (для продакшена) 