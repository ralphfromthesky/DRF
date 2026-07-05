from ..models.models import Inventory
from ..serializers.serializer import InventorySerializer
from rest_framework.viewsets import ModelViewSet


class InventoryViewset(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class  = InventorySerializer