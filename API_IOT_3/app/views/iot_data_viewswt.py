from rest_framework import viewsets
from app.models.iot_data_model import IOTData
from app.serializers.iot_data_serializer import IOTDataSerializer


class IOTDataViewSet(viewsets.ModelViewSet):
  queryset = IOTData.objects.all()
  serializer_class = IOTDataSerializer
  
  