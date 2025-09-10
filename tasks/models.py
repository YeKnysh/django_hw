from django.db import models


class Category(models.Model):
    """Категория выполнения задачи."""
    name = models.CharField(
        max_length=120,
        unique=True,
        verbose_name="Название категории"
    )

    class Meta:
        db_table = "task_manager_category"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    """Задача. Название уникально в рамках дня создания."""

    class Status(models.TextChoices):
        NEW = "new", "New"
        IN_PROGRESS = "in_progress", "In progress"
        PENDING = "pending", "Pending"
        BLOCKED = "blocked", "Blocked"
        DONE = "done", "Done"

    title = models.CharField(
        max_length=150,
        verbose_name="Название задачи"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание"
    )
    categories = models.ManyToManyField(
        Category,
        related_name="tasks",
        blank=True,
        verbose_name="Категории"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
        verbose_name="Статус",
    )
    deadline = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дедлайн"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Создано (дата и время)"
    )
    # Отдельное поле только с датой — чтобы сделать понятный уникальный ключ "название в рамках даты":
    created_on = models.DateField(
        auto_now_add=True,
        editable=False,
        verbose_name="Создано (дата)"
    )

    class Meta:
        db_table = "task_manager_task"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ["-created_at"]
        # Уникальность названия в пределах дня:
        constraints = [
            models.UniqueConstraint(
                fields=["title", "created_on"],
                name="uniq_task_title_per_day"
            ),
        ]

    def __str__(self) -> str:
        return self.title

    # --- HW11: helper for admin list (короткое имя в списке) ---
    @property
    def short_title(self) -> str:
        t = self.title or ""
        return t if len(t) <= 10 else f"{t[:10]}..."


class SubTask(models.Model):
    """Подзадача, относится к конкретной Task (один-ко-многим)."""

    class Status(models.TextChoices):
        NEW = "new", "New"
        IN_PROGRESS = "in_progress", "In progress"
        PENDING = "pending", "Pending"
        BLOCKED = "blocked", "Blocked"
        DONE = "done", "Done"

    title = models.CharField(
        max_length=150,
        verbose_name="Название подзадачи"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание"
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,   # если удалим Task — удалятся её SubTask
        related_name="subtasks",
        verbose_name="Задача",
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
        verbose_name="Статус",
    )
    deadline = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дедлайн"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Создано"
    )

    class Meta:
        db_table = "task_manager_subtask"
        verbose_name = "Подзадача"
        verbose_name_plural = "Подзадачи"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title
