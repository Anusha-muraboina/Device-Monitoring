from rest_framework import serializers
from .models import Device,Reading
class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reading
        fields=['timestamp','power','status']
class DeviceSerializer(serializers.ModelSerializer):
    latest_reading=serializers.SerializerMethodField()
    class Meta:
        model=Device
        fields=['id','name','latest_reading']
    def get_latest_reading(self,obj):
        r=obj.readings.first()
        return ReadingSerializer(r).data if r else None
