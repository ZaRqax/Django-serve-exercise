from .models import SensorInfo
from rest_framework import serializers

class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorInfo
        fields = ['id','device_id','sensor_name','sensor_type','house_id','last_message_id']
        