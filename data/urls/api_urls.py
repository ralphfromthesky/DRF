from rest_framework.routers import DefaultRouter
from ..views.api import dataViewset

router = DefaultRouter()
router.register('new_data', dataViewset, basename='new_datas')

urlpatterns = router.urls