from rest_framework import serializers
from ..models import Cars


class CarsSrializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'car_brand', 'car_model', 'production_year', 'car_body', 'engine_type']
