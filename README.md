# WeatherApp

WeatherApp — это API-сервис для регистрации пользователей и получения информации о погоде в их городах.

## Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/Fruzzy07/WeatherApp.git
cd WeatherApp
```

### 2.  Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Настройка базы данных (PostgreSQL)
```bash
CREATE DATABASE weather;
CREATE USER fruzzy WITH PASSWORD '05110202';
ALTER ROLE fruzzy SET client_encoding TO 'utf8';
ALTER ROLE fruzzy SET default_transaction_isolation TO 'read committed';
ALTER ROLE fruzzy SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE weather TO fruzzy;
```

### 4. Применение миграций
```bash
python manage.py migrate
```
### 5. Запуск сервера
```bash
python manage.py runserver
```

## API Документация

### 1. Аутентификация
#### Регистрация пользователя
#### POST /api/auth/register/

#### Тело запроса (JSON):
{
  "username": "tletay",
  "password": "password4567",
  "role": "user",
  "city": "Taraz"
}

#### Ответ (201 Created):

{
  "id": 1,
  "username": "user123",
  "role": "user",
  "city": "London"
}

#### Авторизация (получение JWT-токена)
#### POST /api/auth/login/

#### Тело запроса (JSON):
{
  "username": "tletay",
  "password": "password4567"
}

#### Ответ (200 OK):

{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}

### 2. Получение погоды
#### Добавление города (Только для менеджеров)
#### POST /api/city/add/

#### Тело запроса (JSON):
{
  "name": "Uralsk"
}

#### Ответ (201 Created):

{
  "id": 8,
  "name": "Uralsk"
}

#### Получение погоды Только для аутентифицированных пользователей
#### GET /api/weather/

#### Ответ (200 OK):
{
    "id": 4,
    "city": {
        "id": 5,
        "name": "Hong Kong"
    },
    "temperature": 17.83,
    "description": "overcast clouds",
    "updated_at": "2025-02-19T19:54:39.747498Z"
}

#### Если у пользователя не указан город:

{
  "error": "Город не указан"
}

#### Если город не найден в базе:

{
  "error": "Город не найден в базе данных"
}

#### Если API погоды недоступен:

{
  "error": "Ошибка при запросе погоды: ..."
}


Логика ролей:
user — должен указывать свой город
manager — не указывает город но может добавлять города в базу
