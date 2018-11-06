from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(BreakBeam)
admin.site.register(Magnetometer)
admin.site.register(Proximity)