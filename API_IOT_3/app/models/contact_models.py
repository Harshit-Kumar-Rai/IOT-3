from django.db import models

class ContactType(models.Model):
  contact_type_id = models.AutoField(primary_key=True, db_column='contact_type_id')
  contact_type_name = models.CharField(max_length=80, db_column='contacttypename')
  class Meta:
    managed = False 
    db_table = 'contacttype'
    
  def __str__(self):
    return self.contact_type_name