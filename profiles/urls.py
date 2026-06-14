from django.urls import path
from .views.profiles import showResponse, showRender

urlpatterns = [
    path('newprofile/', showResponse, name='showResponse'),
    path('showprofiles/', showRender, name='showRender')
]