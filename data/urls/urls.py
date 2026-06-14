from django.urls import path
from ..views.data import showResponse
from ..views.viewsTemplates import showTemplates

urlpatterns = [
    path('datas/', showResponse, name='showResponse'),
    path('data_templates/', showTemplates, name='showTemplates')
]