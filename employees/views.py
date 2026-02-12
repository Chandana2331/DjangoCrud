from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Avg, Count
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
import csv

def index(request):
    return render(request, 'employees/index.html')

def admin_dashboard(request):
    return render(request, 'employees/admin_dashboard.html')

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

@api_view(['GET'])
def employee_statistics(request):
    """Get employee statistics"""
    total_employees = Employee.objects.count()
    avg_salary = Employee.objects.aggregate(Avg('salary'))['salary__avg'] or 0
    
    # Department breakdown
    dept_breakdown = Employee.objects.values('department').annotate(
        count=Count('id')
    ).order_by('-count')
    
    # Recent employees (last 5)
    recent_employees = Employee.objects.order_by('-created_at')[:5]
    recent_serializer = EmployeeSerializer(recent_employees, many=True)
    
    return Response({
        'total_employees': total_employees,
        'average_salary': float(avg_salary),
        'department_breakdown': list(dept_breakdown),
        'recent_employees': recent_serializer.data
    })

@api_view(['GET'])
def export_employees(request):
    """Export employees to CSV"""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Email', 'Department', 'Salary', 'Phone', 'Position', 'Hire Date', 'Created At'])
    
    employees = Employee.objects.all()
    for emp in employees:
        writer.writerow([
            emp.id,
            emp.name,
            emp.email,
            emp.department,
            emp.salary,
            emp.phone or '',
            emp.position or '',
            emp.hire_date or '',
            emp.created_at.strftime('%Y-%m-%d %H:%M:%S')
        ])
    
    return response

@api_view(['POST'])
def bulk_delete_employees(request):
    """Bulk delete employees by IDs"""
    ids = request.data.get('ids', [])
    if not ids:
        return Response({'error': 'No IDs provided'}, status=400)
    
    deleted_count = Employee.objects.filter(id__in=ids).delete()[0]
    return Response({'deleted': deleted_count})
