from rest_framework import serializers
from ..models import CarSpace


class CarSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpace
        fields = ['id', 'car_plan', 'car_brand', 'car_model', 'production_year', 'car_body', 'engine_type']
        depth = 1