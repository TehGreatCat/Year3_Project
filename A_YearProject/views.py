from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.


def index(request):
    return render(request, "index.html")


def terminal_show(request):
    terminals = Terminal.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            float(query)
        except ValueError:
            terminals = terminals. \
                filter(Q(type__contains=query) |
                       Q(callsign__contains=query))
        else:
            terminals = terminals.filter(
                Q(passenger_flow__exact=query) |
                Q(id=query)
            ).distinct()
    ctx = {'terminals': terminals}
    return render(request, 'Terminal.html', ctx)


def terminal_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("/terminal")
    form = TerminalzForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/terminal')
    return render(request, 'Terminal_add.html', {'form': form})


def terminal_update(request, id):
    instance = get_object_or_404(Terminal, pk=id)
    terminal = Terminal.objects.get(pk=id)
    form = TerminalzForm(instance=instance)
    if request.method == "POST":
        form = TerminalzForm(request.POST, instance=instance)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            terminal.delete()
            return redirect("/terminal/")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/terminal')
    context = {
        "form": form,
        "title": "Terminal",
        "instance": instance,
    }
    return render(request, 'Terminal_add.html', context)


def runway_show(request):
    runways = Runway.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            runways = runways.filter(
                Q(length__exact=query) |
                Q(maxweight__exact=query) |
                Q(flight_field=query)
            ).distinct()
        except ValueError as e:
            print(e)
    ctx = {'runways': runways}
    return render(request, 'Runway.html', ctx)


def runway_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("runway")
    form = RunwayForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/runway')
    return render(request, 'Runway_add.html', {'form': form})


def runway_update(request, id):
    instance = get_object_or_404(Runway, pk=id)
    runway = Runway.objects.get(pk=id)
    form = RunwayForm(instance=instance)
    if request.method == "POST":
        form = RunwayForm(request.POST, instance=instance)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            runway.delete()
            return redirect("runway")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/runway')
    context = {
        "form": form,
        "title": "Runway",
        "instance": instance,
    }
    return render(request, 'Runway_add.html', context)


def plane_show(request):
    planes = Plane.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            float(query)
        except ValueError:
            planes = planes.\
                filter(Q(model__contains=query) |
                       Q(type__contains=query))
        else:
            planes = planes.filter(
                Q(num_of_seats__exact=query) |
                Q(length__exact=query) |
                Q(wingspan__exact=query) |
                Q(weight__exact=query)
            ).distinct()
    ctx = {'planes': planes}
    return render(request, 'Plane.html', ctx)


def plane_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("/planes")
    form = PlaneForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/planes')
    return render(request, 'Plane_add.html', {'form': form})


def plane_update(request, model):
    instance = get_object_or_404(Plane, pk=model)
    plane = Plane.objects.get(pk=model)
    form = PlaneForm(instance=instance)
    if request.method == "POST":
        form = PlaneForm(request.POST, instance=instance)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            plane.delete()
            return redirect("/planes")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/planes')
    context = {
        "form": form,
        "title": "Plane",
        "instance": instance,
    }
    return render(request, 'Plane_add.html', context)


def gates_show(request):
    gates = Gates.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            float(query)
        except ValueError:
            gates = gates.\
                filter(Q(type__contains=query))
        else:
            gates = gates.filter(
                Q(throughput__exact=query) |
                Q(id__exact=query) |
                Q(terminal=query) |
                Q(length__exact=query)
            ).distinct()
    ctx = {'gates': gates}
    return render(request, 'Gates.html', ctx)


def gates_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("gate")
    form = GatesForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/gate')
    return render(request, 'Gates_add.html', {'form': form})


def gates_update(request, id):
    instance = get_object_or_404(Gates, pk=id)
    gates = Gates.objects.get(pk=id)
    form = GatesForm(instance=instance)
    if request.method == "POST":
        form = GatesForm(request.POST, instance=instance)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            gates.delete()
            return redirect("/gate")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/gate')
    context = {
        "form": form,
        "title": "Gates",
        "instance": instance,
    }
    return render(request, 'Gates_add.html', context)


def flight_show(request):
    flights = Flight.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            float(query)
        except ValueError:
            flights = flights.filter(Q(plane__contains=query) | Q(airline__contains=query) |
                                     Q(time_of_arrival__exact=query) | Q(time_of_departure__exact=query))
        else:
            flights = flights.filter(
                Q(id__exact=query) |
                Q(gates__exact=query) |
                Q(runway__exact=query)
            ).distinct()
    ctx = {'flights': flights}
    return render(request, 'Flight.html', ctx)


def flight_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("flight")
    form = FlightForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/flight')
    return render(request, 'flight_add.html', {'form': form})


def flight_update(request, id):
    instance = get_object_or_404(Flight, pk=id)
    flight = Flight.objects.get(pk=id)
    form = FlightForm(instance=instance)
    if request.method == "POST":
        form = FlightForm(request.POST, instance=instance)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            flight.delete()
            return redirect("flight")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/flight')
    context = {
        "form": form,
        "title": "Flight",
        "instance": instance,
    }
    return render(request, 'Flight_add.html', context)


def storage_show(request):
    storage = Storage.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            storage = storage.filter(
                Q(id__exact=query) |
                Q(height__exact=query) |
                Q(volume__exact=query) |
                Q(temperature__exact=query) |
                Q(terminal=query)
            ).distinct()
        except ValueError as e:
            print(e)
    ctx = {'storage': storage}
    print(ctx)
    return render(request, 'Storage.html', ctx)


def storage_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("/storage")
    form = StorageForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/storage')
    return render(request, 'Storage_add.html', {'form': form})


def storage_update(request, id):
    instance = get_object_or_404(Storage, pk=id)
    storage = Storage.objects.get(pk=id)
    form = StorageForm(instance=instance)
    if request.method == "POST":
        form = StorageForm(request.POST, instance=instance)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            storage.delete()
            return redirect("/storage")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/storage')
    context = {
        "form": form,
        "title": "Storage",
        "instance": instance,
    }
    return render(request, 'Storage_add.html', context)


def control_tower_show(request):
    towers = ControlTower.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            towers = towers.filter(
                Q(id__exact=query) |
                Q(radius__exact=query) |
                Q(shortname__contains=query) |
                Q(flight_field=query)
            ).distinct()
        except ValueError as e:
            print(e)
    ctx = {'towers': towers}
    print(ctx)
    return render(request, 'ControlTower.html', ctx)


def control_tower_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("towers")
    form = ControlTowerForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/towers')
    return render(request, 'ControlTower_add.html', {'form': form})


def control_tower_update(request, id):
    instance = get_object_or_404(ControlTower, pk=id)
    towers = ControlTower.objects.get(pk=id)
    form = ControlTowerForm(instance=instance)
    if request.method == "POST":
        form = ControlTowerForm(request.POST, instance=instance)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            towers.delete()
            return redirect("towers")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/towers')
    context = {
        "form": form,
        "title": "ControlTowers",
        "instance": instance,
    }
    return render(request, 'ControlTower_add.html', context)


def flight_field_show(request):
    fields = FlightField.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            float(query)
        except ValueError:
            fields = fields.filter(Q(tarmac_type__contains=query))
        else:
            fields = fields.filter(
                Q(id__exact=query) |
                Q(control_towerid__exact=query) |
                Q(terminal=query)
            ).distinct()
    ctx = {'fields': fields}
    return render(request, 'FlightField.html', ctx)


def flight_field_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("fields")
    form = FlightFieldForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/fields')
    return render(request, 'FlightField_add.html', {'form': form})


def flight_field_update(request, id):
    instance = get_object_or_404(FlightField, pk=id)
    fields = FlightField.objects.get(pk=id)
    form = FlightFieldForm(instance=instance)
    if request.method == "POST":
        form = FlightFieldForm(request.POST, instance=instance)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            fields.delete()
            return redirect("fields")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/fields')
    context = {
        "form": form,
        "title": "FlightFields",
        "instance": instance,
    }
    return render(request, 'FlightField_add.html', context)


def hangar_show(request):
    hangars = Hangar.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            float(query)
        except ValueError:
            hangars = hangars.filter(Q(type__contains=query))
        else:
            hangars = hangars.filter(
                Q(id__exact=query) |
                Q(height__exact=query) |
                Q(width__exact=query) |
                Q(flight_field=query)
            ).distinct()
    ctx = {'hangars': hangars}
    return render(request, 'Hangar.html', ctx)


def hangar_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("hangar")
    form = HangarForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/hangar')
    return render(request, 'Hangar_add.html', {'form': form})


def hangar_update(request, id):
    instance = get_object_or_404(Hangar, pk=id)
    hangars = Hangar.objects.get(pk=id)
    form = HangarForm(instance=instance)
    if request.method == "POST":
        form = HangarForm(request.POST, instance=instance)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            hangars.delete()
            return redirect("hangar")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/hangar')
    context = {
        "form": form,
        "title": "Hangar",
        "instance": instance,
    }
    return render(request, 'Hangar_add.html', context)


def list_of_passengers(request, id):
    passengers = Passenger.objects.all().filter(Q(flight__id=id))
    ctx = {'passengers': passengers}
    return render(request, 'Passengers.html', ctx)


def passenger_show(request):
    passengers = Passenger.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            float(query)
        except ValueError:
            passengers = passengers.filter(Q(first_name__contains=query) |
                                           Q(second_name__contains=query) |
                                           Q(class_field=query))
        else:
            passengers = passengers.filter(
                Q(id__exact=query) |
                Q(seat__exact=query) |
                Q(flight=query)
            ).distinct()
    ctx = {'passengers': passengers}
    return render(request, 'Passengers.html', ctx)


def passenger_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("passengers")
    form = PassengerFrom(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/passengers')
    return render(request, 'Passengers_add.html', {'form': form})


def passenger_update(request, id):
    instance = get_object_or_404(Passenger, pk=id)
    passengers = Passenger.objects.get(pk=id)
    form = PassengerFrom(instance=instance)
    if request.method == "POST":
        form = PassengerFrom(request.POST, instance=instance)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            passengers.delete()
            return redirect("passengers")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/passengers')
    context = {
        "form": form,
        "title": "Passengers",
        "instance": instance,
    }
    return render(request, 'Passengers_add.html', context)


def security_show(request):
    security = Security.objects.all()
    query = request.GET.get('q')
    if query:
        try:
            float(query)
        except ValueError:
            security = security.filter(Q(company__contains=query))
        else:
            security = security.filter(
                Q(id__exact=query) |
                Q(k9_unit=query) |
                Q(access_level__exact=query) |
                Q(terminal=query)
            ).distinct()
    ctx = {'security': security}
    return render(request, 'Security.html', ctx)


def security_add(request):
    if 'delete' in request.POST.keys() and request.POST['delete']:
        return redirect("security")
    form = SecurityFrom(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/security')
    return render(request, 'Security_add.html', {'form': form})


def security_update(request, id):
    instance = get_object_or_404(Security, pk=id)
    security = Security.objects.get(pk=id)
    form = SecurityFrom(instance=instance)
    if request.method == "POST":
        form = SecurityFrom(request.POST, instance=instance)
        if 'delete' in request.POST.keys() and request.POST['delete']:
            security.delete()
            return redirect("/security")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/security')
    context = {
        "form": form,
        "title": "Security",
        "instance": instance,
    }
    return render(request, 'Security_add.html', context)
