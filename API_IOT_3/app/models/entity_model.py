from django.db import models
from app.models.address_model import (Address, AddressType)

class EntityType(models.Model):
    type_id = models.AutoField(primary_key=True, db_column='type_id')
    name = models.CharField(max_length=100, db_column='EntityTypeName', null=True)
    
    def __str__(self):
      return self.name
    
    class Meta:
      managed = False 
      db_table = 'entitytype'

class EntityRole(models.Model):
    role_id = models.AutoField(primary_key=True, db_column='role_id')
    role_name = models.CharField(max_length=100, db_column='rolename', null=True)
    
    def __str__(self):
       return self.role_name
    
    class Meta:
      managed = False 
      db_table = 'entityrole'

class Entity(models.Model):
    entiy_id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=100, db_column='Name')
    short_name = models.CharField(max_length=100, db_column='ShortName')
    long_name = models.CharField(max_length=100, db_column='LongName')
    trade_name = models.CharField(max_length=100, db_column='TradeName')
    type_id = models.ForeignKey(EntityType, on_delete=models.CASCADE, db_column='EntityTypeId', null=True, blank=True) 
    role_id = models.ForeignKey(EntityRole, on_delete=models.CASCADE, db_column='EntityRoleId',  null=True, blank=True) 
    
    class Meta:
      managed = False 
      db_table = 'entity'

class EntityAddress(models.Model):
    entity_id = models.ForeignKey(Entity, on_delete=models.CASCADE, db_column = 'entityid')
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE, db_column = 'id')
    address_type = models.ForeignKey(AddressType, on_delete=models.CASCADE, db_column = 'addresstype')  
    
    class Meta:
      managed = False 
      db_table = 'entityaddress'      