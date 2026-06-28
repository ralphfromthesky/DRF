from rest_framework import serializers
from ..models.models import Employee

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'occupation', 'salary', 'is_active']
        read_only_fields = ['id']