from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('',views.Sensors)
patterns = [
    path('api/', include(router.urls) ),
    path('api-auth',include('rest_framework.urls', namespace='rest_framework')),
]
