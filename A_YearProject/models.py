# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator


class ControlTower(models.Model):
    id = models.AutoField(primary_key=True)
    radius = models.IntegerField(null=True, validators=[MinValueValidator(1),
                                                        MaxValueValidator(10000)])
    shortname = models.CharField(max_length=255, null=True, validators=[MinLengthValidator(3)])
    flight_field = models.ForeignKey('FlightField', models.DO_NOTHING, db_column='flight_field')

    def __str__(self):
        return self.shortname.__str__()

    class Meta:
        managed = False
        db_table = 'control_tower'


class Flight(models.Model):
    id = models.AutoField(primary_key=True)
    time_of_arrival = models.DateTimeField(null=True)
    time_of_departure = models.DateTimeField(null=True)
    gates = models.ForeignKey('Gates', models.DO_NOTHING, db_column='gates')
    runway = models.ForeignKey('Runway', models.DO_NOTHING, db_column='runway')
    airline = models.CharField(max_length=255, null=True, validators=[MinLengthValidator(1)])
    plane = models.ForeignKey('Plane', models.DO_NOTHING, db_column='plane')

    def __str__(self):
        return self.airline.__str__() + ' ' + self.time_of_departure.__str__().split(' ')[1]\
               + ' (' + self.plane.type.__str__() + ') ' + self.id.__str__()

    class Meta:
        managed = False
        db_table = 'flight'


class FlightField(models.Model):
    id = models.AutoField(primary_key=True)
    tarmac_type = models.CharField(max_length=255, null=True, validators=[MinLengthValidator(1)])
    terminal = models.ForeignKey('Terminal', models.DO_NOTHING, db_column='terminal')
    area = models.IntegerField(validators=[MinValueValidator(1),
                                           MaxValueValidator(10000)])

    def __str__(self):
        return self.id.__str__() + ' ' + self.terminal.callsign.__str__()

    class Meta:
        managed = False
        db_table = 'flight_field'


class Gates(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255, null=True, validators=[MinLengthValidator(1)])
    length = models.IntegerField(null=True, validators=[MinValueValidator(1),
                                                        MaxValueValidator(500)])
    throughput = models.IntegerField(null=True, validators=[MinValueValidator(1)])
    terminal = models.ForeignKey('Terminal', models.DO_NOTHING, db_column='terminal')

    def __str__(self):
        return self.id.__str__() + ' ' + self.terminal.callsign.__str__() + ' (' + self.type.__str__() + ')'

    class Meta:
        managed = False
        db_table = 'gates'


class Hangar(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255, null=True, validators=[MinLengthValidator(1)])
    height = models.IntegerField(null=True, validators=[MinValueValidator(1),
                                                        MaxValueValidator(500)])
    width = models.IntegerField(null=True, validators=[MinValueValidator(1),
                                                       MaxValueValidator(500)])
    flight_field = models.ForeignKey(FlightField, models.DO_NOTHING, db_column='flight_field')

    def __str__(self):
        return self.id.__str__()

    class Meta:
        managed = False
        db_table = 'hangar'


class Passenger(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, null=True, validators=[MinLengthValidator(1)])
    second_name = models.CharField(max_length=255, null=True, validators=[MinLengthValidator(1)])
    class_field = models.CharField(db_column='class', max_length=255, null=True,
                                   validators=[MinLengthValidator(1)])
    seat = models.IntegerField(null=True, validators=[MinValueValidator(1),
                                                      MaxValueValidator(1000)])
    flight = models.ForeignKey(Flight, models.DO_NOTHING, db_column='flight')

    def __str__(self):
        return self.first_name.__str__() + ' ' + self.second_name.__str__()

    class Meta:
        managed = False
        db_table = 'passenger'


class Plane(models.Model):
    model = models.CharField(primary_key=True, max_length=255, validators=[MinLengthValidator(1)])
    length = models.IntegerField(null=True, validators=[MinValueValidator(1),
                                                        MaxValueValidator(1000)])
    wingspan = models.IntegerField(null=True, validators=[MinValueValidator(1),
                                                          MaxValueValidator(1000)])
    num_of_seats = models.IntegerField(null=True, validators=[MinValueValidator(1),
                                                              MaxValueValidator(1000)])
    weight = models.IntegerField(null=True, validators=[MinValueValidator(1),
                                                        MaxValueValidator(1000)])
    type = models.CharField(max_length=255, null=True, validators=[MinLengthValidator(1)])

    def __str__(self):
        return self.model

    class Meta:
        managed = False
        db_table = 'plane'


class Runway(models.Model):
    id = models.AutoField(primary_key=True)
    length = models.IntegerField(null=True, validators=[MinValueValidator(1),
                                                        MaxValueValidator(10000)])
    tarmac_type = models.CharField(max_length=255, null=True, validators=[MinLengthValidator(1)])
    max_weight = models.IntegerField(null=True, validators=[MinValueValidator(1),
                                                            MaxValueValidator(10000000)])
    flight_field = models.ForeignKey(FlightField, models.DO_NOTHING, db_column='flight_field')

    def __str__(self):
        return self.id.__str__() + ' ' + self.flight_field.terminal.callsign.__str__()

    class Meta:
        managed = False
        db_table = 'runway'


class Security(models.Model):
    id = models.AutoField(primary_key=True)
    access_level = models.IntegerField(null=True, validators=[MinValueValidator(1),
                                                              MaxValueValidator(10)])
    k9_unit = models.NullBooleanField()
    company = models.CharField(max_length=255, null=True
                               , validators=[MinLengthValidator(1)])
    terminal = models.ForeignKey('Terminal', models.DO_NOTHING, db_column='terminal')

    def __str__(self):
        return self.id.__str__() + ' ' + self.company.__str__()

    class Meta:
        managed = False
        db_table = 'security'


class Storage(models.Model):
    id = models.AutoField(primary_key=True)
    volume = models.IntegerField(null=True, validators=[MinValueValidator(1)])
    height = models.IntegerField(null=True, validators=[MinValueValidator(1)])
    temperature = models.IntegerField(null=True, validators=[MinValueValidator(-60),
                                                             MaxValueValidator(451)])
    terminal = models.ForeignKey('Terminal', models.DO_NOTHING, db_column='terminal')

    def __str__(self):
        return self.id.__str__()

    class Meta:
        managed = False
        db_table = 'storage'


class Terminal(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255, null=True, validators=[MinLengthValidator(1)])
    callsign = models.CharField(max_length=255, null=True, validators=[MinLengthValidator(1)])
    passenger_flow = models.IntegerField(null=True, validators=[MinValueValidator(1),
                                                                MaxValueValidator(100000000)])

    def __str__(self):
        return self.id.__str__() + ' ' + self.callsign.__str__()

    class Meta:
        managed = False
        db_table = 'terminal'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
