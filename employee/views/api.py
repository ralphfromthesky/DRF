from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models.models import Employee
from ..serializers.serializers import EmployeeSerializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            self.perform_create(serializer)
            
            return Response({
                "status": 200,
                "message" : "success",
                "data" : serializer.data
            }, status=status.HTTP_200_OK)
                
        return Response({
            "status": 400,
            "message": "error",
            "error": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
