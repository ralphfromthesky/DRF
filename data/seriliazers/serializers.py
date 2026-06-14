from rest_framework import serializers
from ..models.models import datas

class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = datas
        fields = ['id', 'descriptions', 'data', 'is_active']
        read_only_fields = ["id"]