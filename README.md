### Это тестовое задание для реализации CRUD-приложения с использованием FastAPI. В приложении реализованы функции для работы с книгами и авторами

## Установка

### Требования
- Python 3.10+
- PostgreSQL
- Виртуальное окружение (опционально)

### Клонирование репозитория
```
git clone https://github.com/Equialy/library_patres.git
cd library_patres
```



### Развертывание через Docker

Для использование Docker-compose выполните следующие шаги находясь в корне проекта:
```
docker compose build
```
```
docker compose up
```

- Запустится база и прогонятся миграции автоматически.

```
Октрыть в браузере по адресу http://localhost:8003/docs
```



### Локальное развертывание
Настройка окружения
1. Создайте виртуальное окружение:
```
python -m venv venv
source venv/bin/activate  # В Windows: venv\Scripts\activate
```

2. Установите зависимости:
```
pip install -r requirements.txt
```
3. Создайте файл .env в корневой папке проекта со следующим содержимым:
```
#DataBase
PG_HOST=youre_host
PG_PORT=youre_port
PG_USER=your_user
PG_PASSWORD=youer_password
PG_DB_NAME=your_db_name

#AuthSecrets
SECRET_KEY=your_secret_key
ALGORITHM=your_algorithm
CRYPT_SCHEMA=your_schema
```
4. Применение миграций базы данных:
```
alembic upgrade head
```
6. Запуск сервера:
```
uvicorn src.main:app --reload
```
