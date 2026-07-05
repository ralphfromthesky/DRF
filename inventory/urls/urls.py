from rest_framework.routers import DefaultRouter
from django.urls import path, include
from ..views.api import InventoryViewset

router = DefaultRouter()
router.register('new_inventory', InventoryViewset , basename='InventoryViewset')

urlpatterns = [
    path('', include(router.urls))
]

