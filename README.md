# Django Homework (Cumulative Project)

## HW1
- Django project created (package: `django_hw`)
- .env + django-environ: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`
- DB switch via env `MYSQL` (0=SQLite, 1=MySQL)
- App `core` + route `/` and `/hello/` → "Hello, Yevhen!"
- Requirements: `requirements.txt`
- Git initialized

### How to run
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


## HW2
**Что добавлено**
- Приложение `tasks`
- Модели:
  - `Category(name)`
  - `Task(title, description, categories [M2M], status [choices], deadline, created_at, created_on)`
  - `SubTask(title, description, task [FK], status [choices], deadline, created_at)`
- Админка:
  - `TaskAdmin` с фильтрами (status, created_on, categories), поиском, `date_hierarchy`, inline `SubTask`
  - `CategoryAdmin`, `SubTaskAdmin`
- Ограничение уникальности: `(title, created_on)` для Task (название уникально в рамках дня)

**Как запустить**
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # при необходимости
python manage.py runserver 8005    # порт в HW2
