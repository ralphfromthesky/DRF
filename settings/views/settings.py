from django.http import HttpResponse
from django.shortcuts import render

def showResponse(request):
    return HttpResponse('hello ralph this is the setting')

def showTemplates(request):
    return render(request, 'settings/settings.html' )