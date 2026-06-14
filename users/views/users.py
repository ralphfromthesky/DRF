from django.http import HttpResponse
from django.shortcuts import render

def showResponse(request):
    return HttpResponse('hello this is ralph santolorin')