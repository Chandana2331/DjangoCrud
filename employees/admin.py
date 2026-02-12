from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department', 'email', 'salary', 'created_at')
    search_fields = ('name', 'email', 'department')
    list_filter = ('department', 'created_at')
    ordering = ('-created_at',)

admin.site.register(Employee, EmployeeAdmin)
