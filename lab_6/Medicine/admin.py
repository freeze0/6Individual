from django.contrib import admin

from .models import *

admin.site.register(Human)
admin.site.register(Doctor)
admin.site.register(Appointment)