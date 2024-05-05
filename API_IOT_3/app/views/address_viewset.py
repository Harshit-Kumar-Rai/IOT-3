from rest_framework import viewsets
from app.models.address_model import Address
from app.serializers.address_serializer import AddressSerializer
from app.serializers.address_serializer import CitySerializer, StateSerializer, WardSerializer
from app.models.address_model import City, State, Ward
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection

#viewset
class AddressViewSet(viewsets.ModelViewSet):
  queryset = Address.objects.all()
  serializer_class = AddressSerializer
  
  
#custome viewset

#get all state based on country
class GetAllStateAddressCustomView(APIView):
  def get(self,  request, country_id):
    states = State.objects.filter(country = country_id)
    serializer = StateSerializer(states, many=True)
    return Response(serializer.data)


#get all city based on state
class GetAllCityOfStateAddressCustomView(APIView):
  def get(self, request, state_id):
    cities = City.objects.filter(state_id=state_id).order_by('-name')
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)
  
#get all ward based on state

class GetAllWardOfStateAddressCustomeView(APIView):
  def get(self, request, state_id):
    ward = Ward.objects.filter(state_id=state_id)
    serializer = WardSerializer(ward, many=True)
    return Response(serializer.data)


'''Resut Through Joins'''
class GetAddressThroughJoin(APIView):
  def get(self, request, *args, **kwargs):
    query = f"select cityname, stateId from city join state on city.stateId = state.State_Id where city.stateId = {1};"
    
    with connection.cursor() as cursor:
      cursor.execute(query)
      columns = [col[0] for col in cursor.description]
      
      results = [dict(zip(columns, row)) for row in cursor.fetchall()]
      return Response(results)