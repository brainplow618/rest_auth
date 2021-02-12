from rest_framework import viewsets
from django.http import HttpResponse
import requests
from .models import Forecast
from .serializers import ForeastSerializer


class WeatherViewset(viewsets.ModelViewSet):
    serializer_class = ForeastSerializer

    def get_queryset(self):
        data = Forecast.objects.all()
        return data

    def _get_weather_data(self):
        url = " "
        api_request = requests.get(url)

        try:
            api_request.raise_for_status()
            return api_request.json()
        except:
            return None