from django import forms
from .models import (Vehicle, Parcel, Hire, Sacco)


class VehicleBookingForm(forms.ModelForm):
    class Meta:
        model = Hire
        widgets = {
            'pickUpDate': forms.DateInput(
                format='%dd/%mm/%yyyy',
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }),
            'returnDate': forms.DateInput(
                format='%dd/%mm/%yyyy',
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }),
            'number': forms.NumberInput(
                attrs={
                    'class': 'form-control'}),
            'location': forms.Select(
                attrs={
                    'class': 'form-control'}),
            'destination': forms.Select(
                attrs={
                    'class': 'form-control'}),
            'vehicleMake': forms.Select(
                attrs={
                    'class': 'form-control'}),
        }
        fields = '__all__'


class SeatBookingForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        widgets = {
            'departureTime': forms.TimeInput(
                format='%H:%M',
                attrs={
                    'class': 'form-control',
                    'type': 'time'}),
            'destination': forms.Select(
                attrs={
                    'class': 'form-control'}),
            'source': forms.Select(
                attrs={
                    'class': 'form-control'})}
        fields = ['source', 'destination', 'departureTime']


class ParcelBookingForm(forms.ModelForm):
    class Meta:
        model = Parcel
        exclude = ['datePlaced', 'saccoName']
        widgets = {
            'fragile': forms.Select(
                attrs={
                    'class': 'form-control'}),
            'destination': forms.Select(
                attrs={
                    'class': 'form-control'}),
            'recipientId': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'number'}),
            'recipient': forms.TextInput(
                attrs={
                    'class': 'form-control'}),
            'source': forms.Select(
                attrs={
                    'class': 'form-control'}),
            'weight': forms.NumberInput(
                attrs={
                    'class': 'form-control'}),
        }


class SaccoRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'}))

    class Meta:
        model = Sacco
        exclude = ['hasBeenAdded']
        widgets = {
            'location': forms.CheckboxSelectMultiple(
                attrs={
                    'class': 'form-check-input'}),
            'saccoName': forms.TextInput(
                attrs={
                    'class': 'form-control'}),
            'num': forms.NumberInput(
                attrs={
                    'class': 'form-control'}),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'}),
        }
        errors = {
            'saccoName': 'This sacco has been registered',
            'username': 'The username already exists'}


class VehicleAdditionForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'numberPlate',
            'capacity',
            'source',
            'destination',
            'departureTime',
            'arrivalTime',
            'vehicleMake',
            'seatType',
            'seatPrice']
        widgets = {
            'numberPlate': forms.TextInput(
                attrs={
                    'class': 'form-control'}),
            'capacity': forms.NumberInput(
                attrs={
                    'class': 'form-control'}),
            'destination': forms.Select(
                attrs={
                    'class': 'form-control'}),
            'source': forms.Select(
                attrs={
                    'class': 'form-control'}),
            'departureTime': forms.TimeInput(
                format='%H:%M',
                attrs={
                    'class': 'form-control',
                    'type': 'time'}),
            'arrivalTime': forms.TimeInput(
                format='%H:%M',
                attrs={
                    'class': 'form-control',
                    'type': 'time'}),
            'vehicleMake': forms.Select(
                attrs={
                    'class': 'form-control'}),
            'seatType': forms.Select(
                attrs={
                    'class': 'form-control'}),
            'seatPrice': forms.NumberInput(
                attrs={
                    'class': 'form-control'}),
        }
        errors = {'numberPlate': 'Wrong number plate format', }


class VehicleModificationForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'source',
            'destination',
            'departureTime',
            'arrivalTime',
            'seatType',
            'seatPrice']
        widgets = {
            'destination': forms.Select(
                attrs={
                    'class': 'form-control',
                    'value': '{{form.destination}}'}),
            'source': forms.Select(
                attrs={
                    'class': 'form-control',
                    'value': '{{form.source}}'}),
            'departureTime': forms.TimeInput(
                format='%H:%M',
                attrs={
                    'class': 'form-control',
                    'type': 'time',
                    'value': '{{form.departureTime}}'}),
            'arrivalTime': forms.TimeInput(
                format='%H:%M',
                attrs={
                    'class': 'form-control',
                    'type': 'time',
                    'value': '{{form.arrivalTime}}'}),
            'seatType': forms.Select(
                attrs={
                    'class': 'form-control',
                    'value': '{{form.seatType}'}),
            'seatPrice': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'value': '{{form.seatPrice}}'}),
        }


class LoginForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control  mb-2 mr-sm-2',
                'placeholder': 'Password'}))

    class Meta:
        model = Sacco
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control  mb-2 mr-sm-2',
                    'placeholder': 'Username'}),
        }
        errors = {'userName': 'Incorrect username or password', }
        fields = ['username', 'password']
