# from django.shortcuts import render

# # Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello_api(request):
    messages = 'sample response'
    return Response({
        
        "message": messages,
        "status": True
        })
