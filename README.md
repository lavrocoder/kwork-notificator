# Режим разработки
## Обязательные переменные окружения
1. `TELEGRAM_TOKEN` - Токен телеграм бота.
2. `USER_ID` - ID пользователя кому отсылать уведомления

## Не обязательные переменные окружения
1. `DB_TYPE` - Тип БД. Варианты `sqlite`, `postgresql`. По умолчанию `sqlite`. Если хотите использовать `postgresql`, укажите его. Дополнительные переменные указывать не обязательно. 
2. `POSTGRES_HOST` - Хост БД для `postgresql`. По умолчанию `localhost`
3. `POSTGRES_PORT` - Порт БД для `postgresql`. По умолчанию `5432`
4. `POSTGRES_USER` - Пользователь БД для `postgresql`. По умолчанию `db_user`
5. `POSTGRES_PASSWORD` - Пароль БД для `postgresql`. По умолчанию `db_password`
6. `POSTGRES_DB` - Название БД для `postgresql`. По умолчанию `db_name`

## Полезные команды во время разработки
- `alembic init app/alembic` - Инициализирует alembic
- `docker run -d --name kwork_db -e POSTGRES_USER=db_user -e POSTGRES_PASSWORD=db_password -e POSTGRES_DB=db_name -p 5432:5432 postgres:16-alpine` - Создаёт БД для разработки
- `alembic revision --autogenerate -m "Initial tables"` - Создаёт миграцию
- `alembic upgrade head` - Проводит миграцию
