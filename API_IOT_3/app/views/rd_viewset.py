from rest_framework import viewsets
from app.models.rd_model import RD
from app.serializers.rd_serializer import RDSerializer


class RDViewSet(viewsets.ModelViewSet):
  queryset = RD.objects.all()
  serializer_class = RDSerializer