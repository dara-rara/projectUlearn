from django.contrib import admin
from .models import *

admin.site.register([
    Main,
    Demand,
    Geography,
    Skills,
    LastVacancy,
])
