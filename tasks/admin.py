from django.contrib import admin
from .models import Category, Task, SubTask


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 0
    fields = ("title", "status", "deadline", "created_at")
    readonly_fields = ("created_at",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "deadline", "created_on", "created_at")
    list_filter = ("status", "created_on", "categories")
    search_fields = ("title", "description")
    date_hierarchy = "created_on"
    filter_horizontal = ("categories",)
    inlines = [SubTaskInline]
    readonly_fields = ("created_at", "created_on")


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "task", "status", "deadline", "created_at")
    list_filter = ("status", "task")
    search_fields = ("title", "description", "task__title")
    readonly_fields = ("created_at",)
