from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),   # если core есть
    # path("tasks/", include("tasks.urls")),  # добавим при необходимости
]
