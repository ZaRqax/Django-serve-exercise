import sensor
from django.contrib import admin
from .models import SensorInfo
# Register your models here.
class SensorAdmin(admin.ModelAdmin):
    fields= ('sensor_name','sensor_id','sensor_type')

admin.site.register(SensorAdmin,SensorInfo)