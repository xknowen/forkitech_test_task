# 🚀 forkitech_test_task

Асинхронный микросервис на FastAPI с SQLAlchemy ORM и поддержкой PostgreSQL.
Реализует эндпоинты для работы с кошельками, хранит записи в БД, обрабатывает запросы и запускается в Docker-среде.

## ⚙️ Стек технологий

- **Python 3.11**
- **FastAPI**
- **SQLAlchemy (async)**
- **PostgreSQL 15**
- **Docker + Docker Compose**
- **Pytest**
- **TronPy** (работа с блокчейном Tron)

## 🚀 Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/xknowen/FastAPI_test_taskgit.git
cd forkitech_test_task
```

2. Запустите контейнеры:

```bash
docker-compose up --build
```

3. Приложение будет доступно по адресу:
   [http://localhost:8000/docs](http://localhost:8000/docs) — Swagger UI

## 🔌 Переменные окружения

Все переменные заданы в `docker-compose.yml`:

- `DATABASE_URL` — URL основной базы данных
- `DATABASE_TEST_URL` — URL тестовой базы данных

При необходимости можно использовать `.env` файл.

## 🧪 Тестирование

Тесты используют отдельную тестовую БД (`test_db`), которая запускается в Docker на порту `5433`.

1. Убедитесь, что контейнеры работают:

```bash
docker ps
```

2. Запуск тестов:

```bash
docker-compose exec web pytest
```

## 📁 Структура проекта

```text
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── schemas.py
|   ├── tron.py
│   └── routes.py
│
├── tests/
|   ├── test_api.py
│   └── test_db.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 🧑‍💻 Автор

Александр Туршиев
[GitLab](https://github.com/xknowen)
