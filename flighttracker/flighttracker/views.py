import json
from django.shortcuts import render

def index(request):
    return render(request, 'flighttracker/index.html')