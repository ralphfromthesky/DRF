from django.http import HttpResponse
from django.shortcuts import render


def showResponse(request):
    return HttpResponse('this is the profiles')

def showRender(request):
    persons = [
        {'name': 'ralph'},
        {'name': 'shenron'},
        {'name': 'gadwin'},
        {'name': 'ted'},

    ]
    return render(request, 'profiles/index.html', {'data': persons})
