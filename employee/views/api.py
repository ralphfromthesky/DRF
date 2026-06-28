from rest_framework.viewsets import ModelViewSet
from ..models.models import Employee
from ..serializers.serializers import EmployeeSerializers

class EmployeeViewset(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers