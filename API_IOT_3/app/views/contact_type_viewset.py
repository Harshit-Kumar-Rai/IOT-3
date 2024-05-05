from rest_framework import viewsets
from app.serializers.contact_type_serializer import ContactTypeSerializer
from app.models.contact_models import ContactType

class AddressTypeViewSet(viewsets.ModelViewSet):
  queryset = ContactType.objects.all()
  serializer_class = ContactTypeSerializer