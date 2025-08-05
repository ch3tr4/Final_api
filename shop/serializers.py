from rest_framework import serializers

from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Car
        fields = ['id', 'name', 'year','image','price', 'stock', 'vin', 'mile', 'tranmission', 'housepw']