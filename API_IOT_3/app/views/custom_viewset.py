from rest_framework import generics
from app.models.address_model import Address
from app.serializers.address_serializer import AddressSerializer

class AddressListCustom(generics.ListAPIView):
    serializer_class = AddressSerializer

    def get_queryset(self):
        entity_id = self.kwargs['entity_id']
        return Address.objects.filter(entity_id=entity_id)