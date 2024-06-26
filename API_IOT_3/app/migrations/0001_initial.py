# Generated by Django 4.1.7 on 2024-05-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "address_line_1",
                    models.CharField(db_column="addressline1", max_length=100),
                ),
                (
                    "address_line_2",
                    models.CharField(db_column="Addressline2", max_length=100),
                ),
                ("pincode", models.CharField(db_column="pincode", max_length=15)),
                ("city_id", models.IntegerField(db_column="CityId")),
                ("state_id", models.IntegerField(db_column="stateid")),
                ("ward_id", models.IntegerField(db_column="wardid")),
                ("region_id", models.IntegerField(db_column="regionid")),
                ("zone_id", models.IntegerField(db_column="zoneid")),
                ("latitude", models.FloatField(db_column="latitude")),
                ("longitude", models.FloatField(db_column="longitude")),
            ],
            options={
                "db_table": "address",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AddressContact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "db_table": "address_contact",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AddressType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_column="name", max_length=100)),
            ],
            options={
                "db_table": "address_type",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_column="name", max_length=100)),
            ],
            options={
                "db_table": "city",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ContactType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "contact_type_name",
                    models.CharField(db_column="contact_type_name", max_length=80),
                ),
            ],
            options={
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_column="name", max_length=100)),
            ],
            options={
                "db_table": "country",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Device",
            fields=[
                (
                    "id",
                    models.AutoField(db_column="id", primary_key=True, serialize=False),
                ),
                ("name", models.CharField(db_column="name", max_length=100)),
                ("imei", models.CharField(db_column="imie", max_length=100)),
                ("parent_id", models.CharField(db_column="parentid", max_length=100)),
                ("model", models.CharField(db_column="model", max_length=100)),
                (
                    "device_serial_no",
                    models.CharField(db_column="deviceserialno", max_length=100),
                ),
            ],
            options={
                "db_table": "device",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DeviceInstallation",
            fields=[
                (
                    "device_installation_id",
                    models.AutoField(db_column="id", primary_key=True, serialize=False),
                ),
                (
                    "installation_date_time",
                    models.DateTimeField(
                        auto_now_add=True, db_column="installationdatetime"
                    ),
                ),
            ],
            options={
                "db_table": "deviceinstallation",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DeviceInstallImage",
            fields=[
                (
                    "install_image_id",
                    models.AutoField(db_column="id", primary_key=True, serialize=False),
                ),
                (
                    "image_url",
                    models.URLField(
                        blank=True, db_column="imageurl", null=True, unique=True
                    ),
                ),
            ],
            options={
                "db_table": "deviceinstallationimages",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DeviceType",
            fields=[
                (
                    "device_type_id",
                    models.AutoField(db_column="id", primary_key=True, serialize=False),
                ),
                (
                    "sending_freq_sec",
                    models.DecimalField(
                        db_column="sending_ferq", decimal_places=2, max_digits=10
                    ),
                ),
                (
                    "position_acuracy_mtr",
                    models.IntegerField(db_column="position_accuracy", max_length=100),
                ),
                (
                    "protection_rating",
                    models.CharField(db_column="prtection_rating", max_length=100),
                ),
                (
                    "operating_voltage_vlt",
                    models.CharField(db_column="opreating_voltage", max_length=100),
                ),
                (
                    "hot_start_ses",
                    models.CharField(db_column="hot_start", max_length=100),
                ),
                (
                    "warm_start_ses",
                    models.CharField(db_column="warm_start", max_length=100),
                ),
                (
                    "cold_start_ses",
                    models.CharField(db_column="cold_start", max_length=100),
                ),
                (
                    "humidity_level_pc",
                    models.CharField(db_column="humidity_level", max_length=100),
                ),
                (
                    "operating_temp_c",
                    models.CharField(db_column="opreating_temp", max_length=100),
                ),
                (
                    "senstivity_dbm",
                    models.CharField(db_column="sensitivity", max_length=100),
                ),
                (
                    "active_mode_peak_amp",
                    models.CharField(db_column="active_mode_peak", max_length=100),
                ),
                (
                    "active_mode_avg_mamp",
                    models.CharField(db_column="active_mode_avg", max_length=100),
                ),
                (
                    "battery_backup_hrs",
                    models.CharField(db_column="battery_backup", max_length=100),
                ),
                (
                    "sleep_mode_ma",
                    models.CharField(db_column="sleep_mode", max_length=100),
                ),
                ("usb_port", models.CharField(db_column="usb_port", max_length=100)),
                (
                    "GPS_reciver",
                    models.CharField(db_column="GPS_reciver", max_length=100),
                ),
                (
                    "GPS_accuracy_m",
                    models.CharField(db_column="GPS_accuracy", max_length=100),
                ),
                ("protocol", models.CharField(db_column="protocol", max_length=100)),
                ("antenna", models.CharField(db_column="antenna", max_length=100)),
                ("bluetooth", models.CharField(db_column="bluetooth", max_length=100)),
                (
                    "device_life",
                    models.CharField(db_column="device_life", max_length=100),
                ),
                ("Model", models.CharField(db_column="Model", max_length=100)),
                (
                    "battery_mah",
                    models.CharField(db_column="Battery_mah", max_length=100),
                ),
                ("channels", models.CharField(db_column="Channels", max_length=100)),
                ("band_2g", models.CharField(db_column="Band_2G", max_length=100)),
                ("rf_power", models.CharField(db_column="rfpower", max_length=100)),
                (
                    "data_coding",
                    models.CharField(db_column="Datacoding", max_length=100),
                ),
                (
                    "comm_protocol",
                    models.CharField(db_column="CommProtocol", max_length=100),
                ),
                (
                    "digital_input",
                    models.CharField(db_column="Digital Input", max_length=100),
                ),
                (
                    "digital_output",
                    models.CharField(db_column="Digital output", max_length=100),
                ),
                (
                    "analog_input",
                    models.CharField(db_column="Analog Input", max_length=100),
                ),
                ("memory", models.CharField(db_column="Memory", max_length=100)),
                (
                    "firmware_update",
                    models.CharField(db_column="Firmwareupdate", max_length=100),
                ),
                ("sms", models.CharField(db_column="Sms", max_length=100)),
                (
                    "certificates",
                    models.CharField(db_column="certificates", max_length=100),
                ),
                ("sos", models.CharField(db_column="Sos", max_length=100)),
            ],
            options={
                "db_table": "devicetype",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Entity",
            fields=[
                (
                    "entiy_id",
                    models.AutoField(db_column="id", primary_key=True, serialize=False),
                ),
                ("name", models.CharField(db_column="Name", max_length=100)),
                ("short_name", models.CharField(db_column="ShortName", max_length=100)),
                ("long_name", models.CharField(db_column="LongName", max_length=100)),
                ("trade_name", models.CharField(db_column="TradeName", max_length=100)),
            ],
            options={
                "db_table": "entity",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="EntityAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "db_table": "entity_address",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="EntityRd",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "db_table": "entity_rd",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="EntityRole",
            fields=[
                (
                    "role_id",
                    models.AutoField(
                        db_column="role_id", primary_key=True, serialize=False
                    ),
                ),
                (
                    "role_name",
                    models.CharField(db_column="rolename", max_length=100, null=True),
                ),
            ],
            options={
                "db_table": "entityrole",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="EntityType",
            fields=[
                (
                    "type_id",
                    models.AutoField(
                        db_column="type_id", primary_key=True, serialize=False
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_column="EntityTypeName", max_length=100, null=True
                    ),
                ),
            ],
            options={
                "db_table": "entitytype",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="IOTData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "temprature",
                    models.CharField(db_column="temperature", max_length=100),
                ),
                ("lattitude", models.CharField(db_column="lattitude", max_length=100)),
                ("longitude", models.CharField(db_column="longitude", max_length=100)),
                ("imei", models.CharField(db_column="imie", max_length=100)),
                (
                    "is_charging",
                    models.CharField(db_column="ischarging", max_length=100),
                ),
                (
                    "battery_voltage",
                    models.CharField(db_column="batteryvoltage", max_length=100),
                ),
                ("humidity", models.CharField(db_column="humidity", max_length=100)),
                (
                    "signal_strength",
                    models.CharField(db_column="signalstrength", max_length=100),
                ),
                (
                    "last_reporting_time",
                    models.CharField(db_column="lastreportingtime", max_length=100),
                ),
                (
                    "received_data_packet",
                    models.CharField(db_column="receiveddatapacket", max_length=100),
                ),
            ],
            options={
                "db_table": "iotdata",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "location_name",
                    models.CharField(db_column="locationname", max_length=100),
                ),
            ],
            options={
                "db_table": "location",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "person_id",
                    models.AutoField(db_column="id", primary_key=True, serialize=False),
                ),
                ("first_name", models.CharField(db_column="firstname", max_length=100)),
                ("last_name", models.CharField(db_column="lastname", max_length=100)),
                (
                    "mobile_number",
                    models.CharField(db_column="mobilenumber", max_length=20),
                ),
                ("email", models.EmailField(db_column="email", max_length=254)),
                ("image_url", models.URLField(db_column="imageurl")),
            ],
            options={
                "db_table": "person",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="RD",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_column="name", max_length=100)),
                ("rd_code", models.CharField(db_column="rd_code", max_length=100)),
            ],
            options={
                "db_table": "RD",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="RDLocation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "db_table": "RD_location",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_column="name", max_length=50)),
            ],
            options={
                "db_table": "region",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="State",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_column="name", max_length=80)),
            ],
            options={
                "db_table": "state",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="UserLogin",
            fields=[
                (
                    "login_id",
                    models.AutoField(db_column="id", primary_key=True, serialize=False),
                ),
                ("user_name", models.CharField(db_column="User_fname", max_length=100)),
                (
                    "user_lname",
                    models.CharField(db_column="User_lname", max_length=100),
                ),
                ("password", models.CharField(db_column="Password", max_length=64)),
                ("email", models.EmailField(db_column="Email", max_length=254)),
                ("mobile_no", models.CharField(db_column="Mobile_no", max_length=13)),
                (
                    "login_date",
                    models.DateTimeField(auto_now=True, db_column="Login_Date"),
                ),
            ],
            options={
                "db_table": "user_login",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Ward",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "ward",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Zone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "zone",
                "managed": False,
            },
        ),
    ]
