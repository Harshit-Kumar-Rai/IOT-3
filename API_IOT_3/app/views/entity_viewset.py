from rest_framework import viewsets
from app.models.entity_model import Entity, EntityRole, EntityType
from app.serializers.entity_serializer import EntitySerializer, EntityRoleSerializer, EntityTypeSerializer
# from rest_framework.throttling import UserRateThrottle

class EntityViewSet(viewsets.ModelViewSet):
  queryset = Entity.objects.all()
  serializer_class = EntitySerializer
  # throttle_classes = [UserRateThrottle]
  
class EntityRoleViewSet(viewsets.ModelViewSet):
  queryset = EntityRole.objects.all()
  serializer_class = EntityRoleSerializer
  
class EntityTypeViewSet(viewsets.ModelViewSet):
  queryset = EntityType.objects.all()
  serializer_class = EntityTypeSerializer
  