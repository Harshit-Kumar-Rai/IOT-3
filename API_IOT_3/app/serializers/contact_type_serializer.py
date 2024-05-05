from rest_framework import serializers
from app.models.contact_models import ContactType

class ContactTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContactType
    fields = '__all__'