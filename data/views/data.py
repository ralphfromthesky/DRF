from django.http import HttpResponse
from django.shortcuts import render

def showResponse(request):
    return HttpResponse('this is the response from data')

