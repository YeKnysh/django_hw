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
