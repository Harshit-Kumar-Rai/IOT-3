from django.db import models
from app.models.user_model import UserLogin #change with django auth model
from app.models.contact_models import ContactType

class Person(models.Model):
  person_id = models.AutoField(primary_key=True, db_column='id')
  first_name = models.CharField(max_length=100, db_column='firstname')
  last_name= models.CharField(max_length=100, db_column='lastname')
  mobile_number = models.CharField(max_length=20, db_column='mobilenumber')
  email = models.EmailField(db_column='email')
  image_url = models.URLField(db_column='imageurl')
  # login_id = models.ForeignKey(UserLogin, on_delete=models.CASCADE, db_column='id')
  contact_type = models.ForeignKey(ContactType, on_delete=models.CASCADE, db_column='contacttype')
  alternate_number = models.CharField(max_length=20, db_column='alternatenumber') 
  
  class Meta:
    managed = False 
    db_table = 'person'