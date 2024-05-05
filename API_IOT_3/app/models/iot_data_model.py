from django.db import models
from app.models.device_model import Device

class IOTData(models.Model):
  temprature = models.CharField(max_length=100, db_column='temperature')
  lattitude = models.CharField(max_length=100, db_column='lattitude')
  longitude = models.CharField(max_length=100, db_column='longitude')
  imei = models.CharField(max_length=100, db_column='imie')
  is_charging = models.CharField(max_length=100, db_column='ischarging')
  battery_voltage = models.CharField(max_length=100, db_column='batteryvoltage')
  humidity = models.CharField(max_length=100, db_column='humidity')
  signal_strength = models.CharField(max_length=100, db_column='signalstrength')
  last_reporting_time = models.CharField(max_length=100, db_column='lastreportingtime')
  device_id = models.ForeignKey(Device,on_delete=models.CASCADE, db_column='deviceid')
  received_data_packet = models.CharField(max_length=100, db_column='receiveddatapacket')
  
  class Meta:
    managed = False 
    db_table = 'iotdata'