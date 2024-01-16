from datetime import datetime

from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_main(request, *args, **kwargs):
    return render(request, 'main.html', {'content': Main.objects.all(), **kwargs})


@csrf_exempt
def get_demand(request, *args, **kwargs):
    return render(request, 'demand.html', {'content': Demand.objects.all(), **kwargs})


@csrf_exempt
def get_geography(request, *args, **kwargs):
    return render(request, 'geography.html', {'content': Geography.objects.all(), **kwargs})


@csrf_exempt
def get_skills(request, *args, **kwargs):
    return render(request, 'skills.html', {'content': Skills.objects.all(), **kwargs})



