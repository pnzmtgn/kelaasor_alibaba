from django.db import models

class Airport(models.Model):
    name = models.CharField(max_length=100)
    N0 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=300)
    phone_number = models.IntegerField()
    open_time = models.TimeField()
    close_time = models.TimeField()

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    capacity = models.IntegerField()
    price = models.FloatField()

