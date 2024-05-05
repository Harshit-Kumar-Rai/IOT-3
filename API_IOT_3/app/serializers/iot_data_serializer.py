from rest_framework import serializers
from app.models.iot_data_model import IOTData

class IOTDataSerializer(serializers.ModelSerializer):
  class Meta:
    model = IOTData
    fields = '__all__'