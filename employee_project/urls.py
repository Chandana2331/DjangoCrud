from django.contrib import admin
from django.urls import path, include
from employees.views import index, admin_dashboard

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("employees.urls")),
    path("", index, name="index"),
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
]
