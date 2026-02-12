from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department', 'salary', 'phone', 'position', 'hire_date', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
    
    def validate_salary(self, value):
        if value < 0:
            raise serializers.ValidationError("Salary cannot be negative")
        if value > 10000000:
            raise serializers.ValidationError("Salary exceeds maximum limit")
        return value
    
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters long")
        return value
