from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=200)
    icon = models.CharField(max_length=10)
