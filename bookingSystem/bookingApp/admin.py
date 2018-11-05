from django.contrib import admin
# Register your models here.
from .models import Sacco, Vehicle, Parcel, Make, Hire, Office, Destination
admin.site.register(Sacco)
admin.site.register(Vehicle)
admin.site.register(Parcel)
admin.site.register(Make)
admin.site.register(Office)
admin.site.register(Destination)
admin.site.register(Hire)
