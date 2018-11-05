from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepageView, name='homepage'),
    path('booking/', views.vehicleBookingView, name='booking'),
    path('parcel/', views.parcelBookingView, name='parcel'),
    path('seats/', views.seatBookingView, name='seat'),
    path('registerSacco/', views.registerSaccoView, name='registerSacco'),
    path('vehicles/add', views.addVehicleView, name='addVehicle'),
    path('accounts/login/', views.loginView, name="logIn"),
    path('accounts/logout/', views.logoutView, name='logout'),
    path('vehicles/', views.saccoVehicleView, name='vehicles'),
    path('vehicles/<pk>', views.vehicleView, name='vehicle_detail'),
    path('vehicles/<pk>/edit', views.vehicleEditView, name='editVehicle'),
    path('vehicles/<pk>/delete', views.deleteVehicleView, name='deleteVehicle')
]
