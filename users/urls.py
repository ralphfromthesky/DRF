from django.urls import path
from .views.users import showResponse

urlpatterns = [
    path('user/', showResponse, name='showResponse')
]