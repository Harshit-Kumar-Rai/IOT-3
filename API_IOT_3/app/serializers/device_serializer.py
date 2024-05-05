from rest_framework import serializers
from app.models.device_model import (DeviceType, Device, DeviceInstallImage, DeviceInstallation)

class DeviceTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = DeviceType
    fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Device
    fields = '__all__'

class DeviceInstallImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = DeviceInstallImage
    fields = '__all__'
    
class DeviceInstallationSerializer(serializers.ModelSerializer):
  class Meta:
    model = DeviceInstallation
    fields = '__all__'