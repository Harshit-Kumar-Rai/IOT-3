from rest_framework import serializers
from app.models.rd_model import (RD, Location, RDLocation, Entity, EntityRd)

class RDSerializer(serializers.ModelSerializer):
  class Meta:
    model = RD
    fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = '__all__'
    
class RDLocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = RDLocation
    fields = '__all__'
    
class EntitySerializer(serializers.ModelSerializer):
  class Meta:
    model = Entity
    fields = '__all__'
    
class EntityRdSerializer(serializers.ModelSerializer):
  class Meta:
    model = EntityRd
    fields = '__all__'