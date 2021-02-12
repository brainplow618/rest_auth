from django.db import models

class Cars(models.Model):
    car_brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    production_year = models.CharField(max_length=100)
    car_body = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=100)

    def __str__(self):
        return self.car_model