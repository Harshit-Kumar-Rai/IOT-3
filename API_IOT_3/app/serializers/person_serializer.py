from rest_framework import serializers
from app.models.person_model import Person
from app.serializers.contact_type_serializer import ContactTypeSerializer

class PersonSerializer(serializers.ModelSerializer):
  
  contact_type_info = ContactTypeSerializer(source='contact_type', read_only=True)
  class Meta:
    model = Person
    fields = '__all__'