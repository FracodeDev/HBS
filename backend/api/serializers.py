from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockModel
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseModel
        fields = '__all__'
