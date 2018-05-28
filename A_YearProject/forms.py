from django.forms import ModelForm
from .models import *


class TerminalzForm(ModelForm):
    class Meta:
        model = Terminal
        fields = ['id', 'type', 'callsign', 'passenger_flow']


class StorageForm(ModelForm):
    class Meta:
        model = Storage
        fields = ['id', 'volume', 'height', 'temperature', 'terminal']


class SecurityFrom(ModelForm):
    class Meta:
        model = Security
        fields = ['id', 'access_level', 'k9_unit', 'company', 'terminal']


class RunwayForm(ModelForm):
    class Meta:
        model = Runway
        fields = ['id', 'length', 'tarmac_type', 'max_weight', 'flight_field']


class PlaneForm(ModelForm):
    class Meta:
        model = Plane
        fields = ['model', 'length', 'wingspan', 'num_of_seats', 'weight', 'type']


class PassengerFrom(ModelForm):
    class Meta:
        model = Passenger
        fields = ['id', 'first_name', 'second_name', 'class_field', 'seat', 'flight']


class HangarForm(ModelForm):
    class Meta:
        model = Hangar
        fields = ['id', 'type', 'height', 'width', 'flight_field']


class GatesForm(ModelForm):
    class Meta:
        model = Gates
        fields = ['id', 'type', 'length', 'throughput', 'terminal']


class FlightFieldForm(ModelForm):
    class Meta:
        model = FlightField
        fields = ['id', 'tarmac_type', 'terminal', 'area']


class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = ['id', 'time_of_arrival', 'time_of_departure', 'gates', 'runway',
                  'airline', 'plane']


class ControlTowerForm(ModelForm):
    class Meta:
        model = ControlTower
        fields = ['id', 'radius', 'shortname', 'flight_field']
