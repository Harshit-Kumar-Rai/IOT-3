from django.db import models
from app.models.person_model import Person

class AddressType(models.Model):
  name = models.CharField(max_length=100, db_column='name')
  
  class Meta:
    managed = False 
    db_table = 'address_type'
    
class Country(models.Model):
  Country_Id = models.AutoField(primary_key=True, db_column='Country_Id')
  name = models.CharField(max_length=100, db_column='name')
  
  class Meta:
    managed = False 
    db_table = 'country'
  
  def __str__(self):
    return self.name
    
class State(models.Model):
  State_Id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=80, db_column='statename')
  country = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='Country_Id')
  
  def __str__(self):
    return self.name
  
  class Meta:
    managed = False 
    db_table = 'state'
    
class Region(models.Model):
  Region_Id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50, db_column='regionname')
  
  def __str__(self):
    return self.name
  
  class Meta:
    managed = False 
    db_table = 'region'
    
class Ward(models.Model):
    Ward_Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_column='wardname')
    state_id = models.ForeignKey(State,on_delete=models.CASCADE, db_column='stateid')
    
    def __str__(self):
      return self.name
    
    class Meta:
      managed = False 
      db_table = 'ward'
      
class Zone(models.Model):
    Zone_Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_column='zonename')
    
    def __str__(self):
      return self.name
    
    class Meta:
      managed = False 
      db_table = 'zone'

class City(models.Model):
    City_Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_column='cityname')
    state_id = models.ForeignKey(State,on_delete=models.CASCADE,db_column='stateid')
    
    def __str__(self):
      return self.name
  
    class Meta:
      managed = False 
      db_table = 'city'

class Address(models.Model):
    address_line_1 = models.CharField(max_length=100, db_column='addressline1')
    address_line_2 = models.CharField(max_length=100, db_column='Addressline2')
    pincode = models.CharField(max_length=15, db_column='pincode')
    
    country_id =models.ForeignKey(Country, on_delete=models.CASCADE, db_column='CountryId')
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, db_column='CityId')
    state_id = models.ForeignKey(State, on_delete=models.CASCADE, db_column='stateid')
    ward_id = models.ForeignKey(Ward, on_delete=models.CASCADE, db_column='wardid')
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='regionid')
    zone_id = models.ForeignKey(Zone, on_delete=models.CASCADE, db_column='zoneid')
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    
    class Meta:
      managed = False 
      db_table = 'address'

class AddressContact(models.Model):
    address_id=models.ForeignKey(Address, on_delete=models.CASCADE, db_column='id')
    person_id=models.ForeignKey(Person, on_delete=models.CASCADE, db_column='person_id')
    
    class Meta:
      managed = False 
      db_table = 'addresscontact'