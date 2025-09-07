from django.contrib import admin
from .models import Category, Task, SubTask


class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 0
    fields = ("title", "status", "deadline", "created_at")
    readonly_fields = ("created_at",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
    list_per_page = 25


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "deadline", "created_at", "categories_list")
    search_fields = ("title", "description", "categories__name")
    list_filter = ("status", "categories", "created_at", "deadline")
    ordering = ("-created_at",)
    list_per_page = 25
    date_hierarchy = "created_at"
    inlines = [SubTaskInline]

    def categories_list(self, obj):
        return ", ".join(obj.categories.values_list("name", flat=True))

    categories_list.short_description = "Категории"


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "task", "status", "deadline", "created_at")
    search_fields = ("title", "description", "task__title")
    list_filter = ("status", "created_at", "deadline", "task")
    ordering = ("-created_at",)
    list_per_page = 25
    date_hierarchy = "created_at"
