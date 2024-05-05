from django.db import models
from app.models.entity_model import *
from app.models.person_model import Person
from app.models.rd_model import Location

class DeviceType(models.Model):
  device_type_id = models.AutoField(primary_key=True, db_column='id')
  sending_freq_sec = models.DecimalField(max_digits=10, decimal_places=2, db_column='sending_ferq')
  position_acuracy_mtr = models.IntegerField(max_length=100, db_column='position_accuracy')
  protection_rating = models.CharField(max_length=100, db_column='prtection_rating')
  operating_voltage_vlt = models.CharField(max_length=100, db_column='opreating_voltage')
  hot_start_ses = models.CharField(max_length=100, db_column='hot_start')
  warm_start_ses = models.CharField(max_length=100, db_column='warm_start')
  cold_start_ses = models.CharField(max_length=100, db_column='cold_start')
  humidity_level_pc = models.CharField(max_length=100, db_column='humidity_level')
  operating_temp_c=models.CharField(max_length=100, db_column='opreating_temp')
  
  senstivity_dbm = models.CharField(max_length=100, db_column='sensitivity')
  active_mode_peak_amp = models.CharField(max_length=100, db_column='active_mode_peak')
  active_mode_avg_mamp = models.CharField(max_length=100, db_column='active_mode_avg')
  battery_backup_hrs = models.CharField(max_length=100, db_column='battery_backup')
  sleep_mode_ma = models.CharField(max_length=100, db_column='sleep_mode')
  usb_port = models.CharField(max_length=100, db_column='usb_port')
  GPS_reciver = models.CharField(max_length=100, db_column='GPS_reciver')
  GPS_accuracy_m = models.CharField(max_length=100, db_column='GPS_accuracy')
  
  protocol = models.CharField(max_length=100, db_column='protocol')
  antenna = models.CharField(max_length=100, db_column='antenna')
  bluetooth = models.CharField(max_length=100, db_column='bluetooth')
  device_life = models.CharField(max_length=100, db_column='device_life')
  Model = models.CharField(max_length=100, db_column='Model')
  battery_mah = models.CharField(max_length=100, db_column='Battery_mah')
  channels = models.CharField(max_length=100, db_column='Channels')
  band_2g = models.CharField(max_length=100, db_column='Band_2G')
  rf_power = models.CharField(max_length=100, db_column='rfpower')
  
  data_coding = models.CharField(max_length=100, db_column='Datacoding')
  comm_protocol = models.CharField(max_length=100, db_column='CommProtocol')
  digital_input = models.CharField(max_length=100, db_column='Digital Input')
  digital_output = models.CharField(max_length=100, db_column='Digital output')
  analog_input = models.CharField(max_length=100, db_column='Analog Input')
  memory = models.CharField(max_length=100, db_column='Memory')
  firmware_update = models.CharField(max_length=100, db_column='Firmwareupdate')
  sms = models.CharField(max_length=100, db_column='Sms')
  certificates = models.CharField(max_length=100, db_column='certificates')
  sos = models.CharField(max_length=100, db_column='Sos')

  class Meta:
    managed = False 
    db_table = 'devicetype'
    
class Device(models.Model):  
  id = models.AutoField(primary_key=True, db_column='id')
  # name = models.CharField(max_length=100, db_column='name')
  imei = models.CharField(max_length=100, db_column='imie')
  device_type_id = models.ForeignKey(DeviceType,on_delete=models.CASCADE, db_column='id')
  parent_id = models.CharField(max_length=100, db_column='parentid')
  # model = models.CharField(max_length=100, db_column='model')
  # device_serial_no = models.CharField(max_length=100, db_column='deviceserialno')
  
  def __str__(self):
    return self.imei
  
  class Meta:
    managed = False 
    db_table = 'device'
    

class DeviceInstallation(models.Model):
    device_installation_id = models.AutoField(primary_key=True, db_column='id')
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE, db_column='deviceid')
    installation_date_time = models.DateTimeField(auto_now_add=True, db_column='installationdatetime')
    # location_id = models.ForeignKey(Location, on_delete=models.CASCADE, db_column='locationid') removed
    approve_person_id = models.ForeignKey(Person, on_delete=models.CASCADE, db_column='id')
    
    class Meta:
      managed = False 
      db_table = 'deviceinstallation'

class DeviceInstallImage(models.Model):
  install_image_id = models.AutoField(primary_key=True, db_column='id')
  installation_id = models.ForeignKey(DeviceInstallation, on_delete=models.CASCADE, db_column='id')
  image_url = models.URLField(max_length=200, unique=True, blank=True, null=True, db_column='imageurl')
  
  class Meta:
    managed = False 
    db_table = 'deviceinstallationimages'