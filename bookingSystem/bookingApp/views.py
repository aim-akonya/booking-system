from django.shortcuts import (render, redirect, get_object_or_404)
from .forms import (
    SeatBookingForm,
    ParcelBookingForm,
    VehicleBookingForm,
    SaccoRegistrationForm,
    VehicleAdditionForm,
    LoginForm,
    VehicleModificationForm)
from bookingApp.models import (
    Hire,
    Sacco,
    Vehicle,
    Destination,
    Office,
    Parcel)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
import datetime
from django.forms.models import model_to_dict
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy
# Create your views here.


def homepageView(request):
    return render(request, 'bookingApp/home.html')


@login_required
def parcelBookingView(request):
    sacco = Sacco.objects.get(username=request.user.username)
    if request.method == "POST":
        form = ParcelBookingForm(request.POST)
        if form.is_valid():
            print(form.data)
            fr = form.cleaned_data['fragile']
            des = Destination.objects.get(location=form.cleaned_data['source'])
            loc = Office.objects.get(location=form.cleaned_data['destination'])
            rec = form.cleaned_data['recipient']
            rid = form.cleaned_data['recipientId']
            wght = form.cleaned_data['weight']
            Parcel.objects.create(
                weight=wght,
                fragile=fr,
                source=loc,
                destination=des,
                recipient=rec,
                recipientId=rid,
                saccoName=sacco)
            message_text = "The parcel with ID " + \
                str(rid) + " has been added successfully"
            messages.success(request, message_text)
            return redirect('parcel')
    else:
        form = ParcelBookingForm()
    return render(request, 'bookingApp/parcel.html',
                  {'form': form, 'sacco': sacco})


@login_required
def saccoParcelView(request):
    parcel_list = Parcel.objects.filter(
        saccoName=Sacco.objects. get(
            username=request.user.username)).order_by('-datePlaced')
    page = int(request.GET.get('page', 1))
    paginator = Paginator(parcel_list, 10)
    try:
        parcels = paginator.page(page)
    except PageNotAnInteger:
        parcels = paginator.page(1)
    except EmptyPage:
        parcels = paginator.page(paginator.num_pages)
    sacco = Sacco.objects.get(username=request.user.username)
    return render(request, 'admins/saccoParcelList.html',
                  {'parcels': parcels, 'sacco': sacco})


def seatBookingView(request):
    if request.method == "POST":
        form = SeatBookingForm(request.POST)
        if form.is_valid():
            dep = form.cleaned_data['departureTime']
            des = form.cleaned_data['destination']
            src = form.cleaned_data['source']
            table_list = [
                model_to_dict(i) for i in Vehicle.objects.filter(
                    departureTime=dep,
                    destination=des,
                    source=src)]
            return render(request,
                          'bookingApp/viewSeats.html',
                          {'table_list': table_list})
    else:
        form = SeatBookingForm()
    return render(request, 'bookingApp/seat.html', {'form': form})


def seatView(request):
    return render(request, 'bookingApp/viewSeats.html')


def vehicleBookingView(request):
    if request.method == "POST":
        form = VehicleBookingForm(request.POST)
        if form.is_valid():
            pic = form.cleaned_data['pickUpDate']
            ret = form.cleaned_data['returnDate']
            loc = Destination.objects.get(
                location=form.cleaned_data['location'])
            des = Office.objects.get(location=form.cleaned_data['destination'])
            num = form.cleaned_data['number']
            veh = form.cleaned_data['vehicleMake']
            if pic < datetime.date.today() or ret < datetime.date.today() or pic < ret:
                form = VehicleBookingForm()
                return render(request,
                              'bookingApp/booking.html',
                              {'form': form})
            else:
                table_list = [
                    model_to_dict(i) for i in Vehicle.objects.filter(
                        source=des, destination=loc, vehicleMake=veh)]
                Hire.objects.create(
                    pickUpDate=pic,
                    returnDate=ret,
                    location=loc,
                    destination=des,
                    number=num,
                    vehicleMake=veh)
                return render(request,
                              'bookingApp/viewVehicles.html',
                              {'table_list': table_list})
    else:
        form = VehicleBookingForm()
    return render(request, 'bookingApp/booking.html', {'form': form})


def vehicleView(request, pk):
    vehicle = get_object_or_404(Vehicle, numberPlate=pk)
    return render(request, 'vehicle.html', {'vehicle': vehicle})


@login_required
def saccoVehicleView(request):
    vehicle_list = Vehicle.objects.filter(
        saccoName=Sacco.objects. get(
            username=request.user.username)).order_by('-dateCreated')
    page = int(request.GET.get('page', 1))
    paginator = Paginator(vehicle_list, 10)
    try:
        vehicles = paginator.page(page)
    except PageNotAnInteger:
        vehicles = paginator.page(1)
    except EmptyPage:
        vehicles = paginator.page(paginator.num_pages)
    sacco = Sacco.objects.get(username=request.user.username)
    return render(request, 'admins/saccoVehicleList.html',
                  {'vehicles': vehicles, 'sacco': sacco})


@login_required
def addVehicleView(request):
    if request.method == "POST":
        form = VehicleAdditionForm(request.POST)
        if form.is_valid():
            sacco = Sacco.objects.get(username=request.user.username)
            num = form.cleaned_data['numberPlate']
            cap = form.cleaned_data['capacity']
            st = form.cleaned_data['seatType']
            sp = form.cleaned_data['seatPrice']
            src = form.cleaned_data['source']
            des = form.cleaned_data['destination']
            dt = form.cleaned_data['departureTime']
            at = form.cleaned_data['arrivalTime']
            vm = form.cleaned_data['vehicleMake']
            Vehicle.objects.create(
                saccoName=sacco,
                capacity=cap,
                numberPlate=num,
                seatType=st,
                seatPrice=sp,
                source=src,
                destination=des,
                arrivalTime=at,
                departureTime=dt,
                vehicleMake=vm,
                hasBeenAdded=True)
            message_text = "The vehicle <a href=" + str(
                reverse_lazy(
                    'editVehicle', args=[
                        str(num)])) + ">" + str(num) + "</a> has been added successfully"
            messages.success(request, mark_safe(message_text))
            return redirect('vehicles')
    else:
        form = VehicleAdditionForm()
    sacco = Sacco.objects.get(username=request.user.username)
    return render(request, 'admins/addVehicle.html',
                  {'form': form, 'sacco': sacco})


@login_required
def deleteVehicleView(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    num = vehicle.numberPlate
    vehicle.delete()
    message_text = "The vehicle " + \
        str(num) + " has been deleted successfully"
    messages.success(request, message_text)
    return redirect('vehicles')


@login_required
def vehicleEditView(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == "POST":
        form = VehicleModificationForm(request.POST, instance=vehicle)
        if form.is_valid():
            vehicle.save()
            return redirect('addVehicle')
    else:
        form = VehicleAdditionForm(instance=vehicle)
    return render(request, 'admins/editVehicle.html', {'form': form})


def registerSaccoView(request):
    if request.method == "POST":
        form = SaccoRegistrationForm(request.POST)
        if form.is_valid():
            testSacco = Sacco.objects.filter(
                saccoName=form.cleaned_data['saccoName'])
            testname = Sacco.objects.filter(
                username=form.cleaned_data['username'])
            if testSacco.count() == 0 and testname.count() == 0:
                User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password'])
                sacco = form.save(commit=False)
                sacco.save()
                return render(
                    request, 'registration/registration_complete.html')
            else:
                message_text = "That sacco or username already exists"
                messages.error(request, message_text)
                form = SaccoRegistrationForm()
                return render(request,
                              'registration/registerSacco.html',
                              {'form': form})
    else:
        form = SaccoRegistrationForm()
    return render(request, 'registration/registerSacco.html', {'form': form})


def loginView(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                sacco = Sacco.objects.get(username=request.user.username)
                return render(request,
                              'bookingApp/home.html',
                              {'sacco': sacco})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def logoutView(request):
    logout(request)
    return redirect('homepage')
