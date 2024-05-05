from rest_framework import serializers
from app.models.entity_model import (EntityType, EntityRole, Entity, EntityAddress)

class EntityTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = EntityType
    fields = '__all__'
    
    
class EntityRoleSerializer(serializers.ModelSerializer):
  class Meta:
    model = EntityRole
    fields = '__all__'
    
class EntitySerializer(serializers.ModelSerializer):

  # type_id = EntityTypeSerializer()
  # role_id = EntityRoleSerializer()
  # type_id = serializers.PrimaryKeyRelatedField(queryset=EntityType.objects.all())
  # role_id = serializers.PrimaryKeyRelatedField(queryset=EntityRole.objects.all())

# 3rd solution
  entity_type = EntityTypeSerializer(source='type_id', read_only=True)
  entity_role = EntityRoleSerializer(source='role_id', read_only=True)  
  
  
  class Meta:
    model = Entity
    fields = '__all__'
    
    # fields = ['id', 'type_id', 'entity_type', 'role_id', 'entity_role', 'name', 'short_name', 'long_name', 'trade_name']
    # primaryKeyField = 'id'
    
  def create(self, validated_data):
        type_id = validated_data.pop('type_id')
        role_id = validated_data.pop('role_id')
        entity = Entity.objects.create(type_id=type_id, role_id=role_id, **validated_data)
        return entity
    
class EntityAddressSerializer(serializers.ModelSerializer):
  class Meta:
    model = EntityAddress
    fields = '__all__'
    
