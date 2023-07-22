from django.contrib import admin
from .models import Tables
from .models import Occupancy

# Register your models here.

admin.site.register(Tables)
admin.site.register(Occupancy)