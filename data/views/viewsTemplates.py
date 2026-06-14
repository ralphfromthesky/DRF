from django.shortcuts import render

def showTemplates(request):
    return render(request, 'index.html')