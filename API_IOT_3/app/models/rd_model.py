from django.db import models
from app.models.address_model import Address
from app.models.entity_model import Entity

class RD(models.Model):
  name = models.CharField(max_length=100, db_column='name')
  rd_code = models.CharField(max_length=100, db_column='rd_code')
  
  class Meta:
    managed = False 
    db_table = 'RD'

class Location(models.Model):
  location_name = models.CharField(max_length=100,  db_column='locationname')
  address_id = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='id')
  
  class Meta:
    managed = False 
    db_table = 'location'
    
  
class RDLocation(models.Model):
  rd_id = models.ForeignKey(RD, on_delete=models.CASCADE, db_column='rdid')
  location_id = models.ForeignKey(Location, on_delete=models.CASCADE, db_column='locationid')
  
  class Meta:
    managed = False 
    db_table = 'RD_location'
    

class EntityRd(models.Model):
  entity_id = models.ForeignKey(Entity, on_delete=models.CASCADE, db_column='entityid')
  rd_id = models.ForeignKey(RD, on_delete=models.CASCADE, db_column='rdid')
  
  class Meta:
    managed = False 
    db_table = 'entity_rd'