from rest_framework import serializers
from app.models.address_model import (AddressType, Country, City, State, Region, Ward, Zone, Address, AddressContact)
from rest_framework.views import APIView
from rest_framework.response import Response

class AddressTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = AddressType
    fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
  class Meta:
    model = Country
    fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
  class Meta:
    model = City
    fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
  class Meta:
    model = State
    fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Region
    fields = '__all__'
        
class WardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ward
    fields = '__all__'
    
class ZoneSerializer(serializers.ModelSerializer):
  class Meta:
    model = Zone
    fields = '__all__'

class AddressContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = AddressContact
    fields = '__all__'
    
class AddressSerializer(serializers.ModelSerializer):
  '''there is no relationship in master DB '''
  country_info = CountrySerializer(source='country_id', read_only=True)
  city_info = CitySerializer(source='city_id', read_only=True)
  state_info = StateSerializer(source='state_id' , read_only=True)
  ward_info = WardSerializer(source='ward_id', read_only=True)
  region_info = RegionSerializer(source='region_id', read_only=True)
  zone_info = ZoneSerializer(source='zone_id', read_only=True)
  
  
  class Meta:
    model = Address
    fields = '__all__'
    
  def create(self, validated_data):
    country_id = validated_data.pop('country_id')
    city_id = validated_data.pop('city_id')
    state_id = validated_data.pop('state_id')
    ward_id = validated_data.pop('ward_id')
    region_id = validated_data.pop('region_id')
    zone_id = validated_data.pop('zone_id')
    address = Address.objects.create(city_id=city_id, state_id=state_id, ward_id=ward_id, region_id=region_id, zone_id=zone_id,country_id=country_id, **validated_data)
    return address
    
''' Address Custome Serializer'''



