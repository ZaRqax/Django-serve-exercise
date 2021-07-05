from django.db.models import query
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import SensorSerializer
from rest_framework import viewsets,permissions
from .models import SensorInfo


class Sensors(viewsets.ModelViewSet):
    queryset = SensorInfo.objects.all()
    serializer_class = SensorSerializer
        
