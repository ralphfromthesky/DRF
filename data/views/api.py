from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models.models import datas
from ..seriliazers.serializers import dataSerializer

class dataViewset(viewsets.ModelViewSet):
    queryset = datas.objects.all()
    serializer_class = dataSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            self.perform_create(serializer)
            
            return Response({
                "status": 200,
                "message": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            "status": 400,
            "message": "error",
            "error": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():
            self.perform_update(serializer)

            return Response({
                "status": 200,
                "message": "update success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "status": 400,
            "message": "error",
            "error": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response({
            "status": 200,
            "message": "deleted successfully"
        }, status=status.HTTP_200_OK)
        
