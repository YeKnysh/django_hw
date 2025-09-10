# Django Homework (Cumulative Project)

Накопительный репозиторий домашних заданий по Django.  
Стек: **Python 3.11+**, **Django 5.2.x**.

---

## HW1 (7)

**Сделано**
- Создан Django-проект: `django_hw`.
- Подключён `.env` через `django-environ`: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`.
- Переключение БД переменной `MYSQL` (0 → SQLite, 1 → MySQL).
- Приложение `core` с маршрутами `/` и `/hello/` (выводит «Hello, Yevhen!»).
- Зависимости: `requirements.txt`.
- Репозиторий инициализирован.

**Как запустить (база)**
~~~bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
~~~

---

## HW2 (8)

**Что добавлено**
- Приложение `tasks`.
- Модели:
  - `Category(name)`
  - `Task(title, description, categories [M2M], status [choices: new/in_progress/pending/blocked/done], deadline, created_at [auto], created_on [auto-date])`
  - `SubTask(title, description, task [FK], status [choices], deadline, created_at [auto])`
- Админка:
  - `TaskAdmin` — фильтры (`status`, `created_on`, `categories`), поиск, `date_hierarchy`, inline `SubTask`.
  - `CategoryAdmin`, `SubTaskAdmin`.
- Ограничение уникальности: `UniqueConstraint(title, created_on)` — одно и то же название задачи в пределах одного дня недопустимо.
- Демо-фикстуры:
  - `tasks/fixtures/initial_tasks.json` — базовые категории.
  - `tasks/fixtures/demo_task.json` — одна задача + две подзадачи.

**Как запустить (HW2 использовали порт 8005)**
~~~bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # при необходимости
python manage.py runserver 8005
~~~
Админка: http://127.0.0.1:8005/admin/

**Загрузка демо-данных (опционально)**
~~~bash
python manage.py loaddata tasks/fixtures/initial_tasks.json
python manage.py loaddata tasks/fixtures/demo_task.json
~~~

---

## HW3 (9)

**Что сделано**
- В моделях:
  - Добавлены методы `__str__` для `Category`, `Task`, `SubTask`.
  - Добавлены `class Meta` для всех моделей:
    - `db_table` (`task_manager_category`, `task_manager_task`, `task_manager_subtask`),
    - `ordering`,
    - `verbose_name`, `verbose_name_plural`.
  - Уникальность:
    - `Category.name` → `unique=True`.
    - `Task` → `UniqueConstraint(title, created_on)` — название уникально в пределах дня.
- В админке:
  - `CategoryAdmin`: список, поиск, сортировка, пагинация.
  - `TaskAdmin`: список с колонкой «Категории», поиск по названию/описанию/категориям, фильтры (`status`, `categories`, `created_at`, `deadline`), пагинация, `date_hierarchy`, **inline SubTask**.
  - `SubTaskAdmin`: список, поиск по названию и `task__title`, фильтры, сортировка, `date_hierarchy`.
- Миграции применены, таблицы переименованы в `task_manager_*`.
- Данные протестированы в админке.

**Как запустить (HW3, порт 8005)**
~~~bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # при необходимости
python manage.py runserver 8005
~~~

**(Опционально) Загрузка фикстур**
~~~bash
python manage.py loaddata tasks/fixtures/initial_tasks.json
python manage.py loaddata tasks/fixtures/demo_task.json
~~~

**Проверка**
- В админке видны разделы: **Задачи / Категории / Подзадачи**.
- Работают поиск, фильтры, сортировка.
- В `Task` можно добавлять `SubTask` через inline.
- Попытка создать вторую задачу с тем же `title` в один и тот же день вызывает ошибку уникальности (ожидаемо).

---

## Проверка работоспособности (кратко)

- В админке видны разделы **Tasks → Задачи/Категории/Подзадачи**.
- В списке задач работает поиск и фильтры (`Статус`, `Создано (дата)`, `Категории`).
- Открывая задачу из фикстуры, видно подзадачи в inline.
- Попытка создать вторую задачу с тем же `title` в тот же день вызывает ошибку уникальности.

---

## Примечания

- Номер порта (например, **8005**) относится только к dev-серверу и **не влияет** на репозиторий. Все ДЗ идут в этом же репо.
- Переключение на MySQL доступно через переменные окружения (`MYSQL=1` и соответствующие `MYSQL_*`).


## HW4(10) — Task Manager: ORM CRUD (порт 8005)

**Что сделано**
- Создание записей через Django ORM: `Task "Prepare presentation"` и две `SubTask`.
- Чтение:
  - все `Task` со статусом `"New"`;
  - все `SubTask` со статусом `"Done"` с просроченным `deadline`.
- Обновление:
  - статус `Task "Prepare presentation"` → `"In progress"`;
  - `deadline` у `SubTask "Gather information"` → на 2 дня назад;
  - описание `SubTask "Create slides"` → `"Create and format presentation slides"`.
- Удаление каскадом: `Task "Prepare presentation"` и все её подзадачи.

**Как воспроизвести (PyCharm / терминал)**
```bash
python manage.py shell
# вставить блок из README "HW4: Django shell скрипт" (см. ниже) и нажать Enter


## HW5(11) — Admin inlines, short title in list, admin action

 Инлайн-формы `SubTask` на странице `Task` в админке (`TabularInline`): можно добавлять/редактировать подзадачи прямо на странице задачи.
- В списке задач отображается **укороченное имя** (`short_title`: первые 10 символов + `…`). Полное название задачи сохраняется для выпадающих списков выбора родителя (через `__str__` модели).
- Кастомный **admin action** в `SubTaskAdmin`: массово переводит выделенные подзадачи в статус **Done**.

**Проверка**
1. `/admin/` → Tasks → открыть задачу → блок SubTasks виден, можно добавлять строки.
2. `/admin/` → Task list: у длинных названий видно усечённое поле `short_title`.
3. `/admin/` → SubTasks → выделить несколько → Actions: *Mark selected subtasks as Done* → статусы меняются на `Done`.

**Технические детали**
- `tasks/models.py`: добавлено `Task.short_title` (`@property`) — миграции не требуются.
- `tasks/admin.py`: `SubTaskInline` подключён к `TaskAdmin`; `list_display` использует `short_title`; в `SubTaskAdmin` добавлен `make_done`.