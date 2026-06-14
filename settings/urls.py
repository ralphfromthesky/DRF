from django.urls import path
from .views.settings import showResponse, showTemplates

urlpatterns = [
    path('newsettings/', showResponse, name='showResponse'),
    path('templates/', showTemplates, name="showTemplates" )
]