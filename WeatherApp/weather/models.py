from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Weather(models.Model):
    city = models.OneToOneField(City, on_delete=models.CASCADE)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

