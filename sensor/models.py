from django.db import models
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets,permissions

SENSORS_TYPE = [(1,'kWh'),(2,'temp'),(3,'humid'),(4,'air_flow')]


class Device(models.Model):
    name = models.CharField(max_length=300,verbose_name='Device name')

class House(models.Model):
    house_name = models.CharField(max_length=300,verbose_name='House name')
    zip_code = models.IntegerField(verbose_name='Zip code')

class SensorInfo(models.Model):
    device_id = models.IntegerField(verbose_name='Device id')
    sensor_name = models.CharField(max_length=300,verbose_name='Sensor name')
    sensor_type = models.IntegerField(choices=SENSORS_TYPE, verbose_name='Sensor Type')
    house_id = models.ForeignKey(House,on_delete=models.CASCADE)
    last_message_id = models.ForeignKey()