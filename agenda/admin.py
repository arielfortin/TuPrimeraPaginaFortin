from django.contrib import admin
from .models import Professional, Service, Shift, Appointment

admin.site.register(Professional)
admin.site.register(Service)
admin.site.register(Shift)
admin.site.register(Appointment)
