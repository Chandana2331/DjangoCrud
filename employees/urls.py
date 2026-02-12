from django.urls import path
from .views import EmployeeListCreateView, EmployeeDetailView, employee_statistics, export_employees, bulk_delete_employees

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/stats/', employee_statistics, name='employee-stats'),
    path('employees/export/', export_employees, name='employee-export'),
    path('employees/bulk-delete/', bulk_delete_employees, name='employee-bulk-delete'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
]
