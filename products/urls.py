from django.urls import path, include
from .views.products import showResponse, showTemplates

urlpatterns = [
    path('product/', showResponse, name='showResponse'),
    path('newproduct/', showTemplates, name='showTemplates'),
]