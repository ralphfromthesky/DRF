from rest_framework.routers import DefaultRouter
from django.urls import path, include
from ..views.api import EmployeeViewset

router = DefaultRouter()
router.register('employee', EmployeeViewset, basename='EmployeeViewset')

urlpatterns = [
    path('', include(router.urls))
]