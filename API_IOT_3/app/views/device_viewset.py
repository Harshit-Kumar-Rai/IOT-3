from rest_framework import viewsets
from app.models.device_model import (Device, DeviceType, DeviceInstallation, DeviceInstallImage)
from app.serializers.device_serializer import (DeviceSerializer, DeviceTypeSerializer, DeviceInstallationSerializer, DeviceInstallImageSerializer)

class DeviceViewSet(viewsets.ModelViewSet):
  queryset = Device.objects.all()
  serializer_class = DeviceSerializer
  
class DeviceTypeViewSet(viewsets.ModelViewSet):
  queryset = DeviceType.objects.all()
  serializer_class = DeviceTypeSerializer
  
class DeviceInstallationViewSet(viewsets.ModelViewSet):
  queryset = DeviceInstallation.objects.all()
  serializer_class = DeviceInstallationSerializer
  
class DeviceInstallImageViewSet(viewsets.ModelViewSet):
  queryset = DeviceInstallImage.objects.all()
  serializer_class = DeviceInstallImageSerializer