from django.db import models

class UserLogin(models.Model):
  login_id = models.AutoField(primary_key=True, db_column='id')
  user_name = models.CharField(max_length=100, db_column='User_fname')
  user_lname = models.CharField(max_length=100, db_column='User_lname')
  password = models.CharField(max_length=64, db_column='Password')
  email = models.EmailField(db_column='Email')
  mobile_no = models.CharField(max_length=13, db_column='Mobile_no')
  login_date = models.DateTimeField(auto_now=True, db_column='Login_Date')
  
  class Meta:
    managed = False 
    db_table = 'user_login'