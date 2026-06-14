from django.http import HttpResponse
from django.shortcuts import render
from ..models import Product

def showResponse(request):
    return HttpResponse('this is the products response')

def showTemplates(request):
    data = Product.objects.all()
    return render(request, 'products/index.html', {'data': data})