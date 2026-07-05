from rest_framework.serializers import Serializer
from ..models.models import Inventory

class InventorySerializer(Serializer):
    class Meta:
        model = Inventory
        fields = ['id', 'item_name', 'descriptions', 'quantity']
        read_only_fields = ['id']