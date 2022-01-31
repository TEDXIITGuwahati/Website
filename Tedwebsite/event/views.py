from django.shortcuts import render
from django.utils import timezone
from datetime import datetime


def events(request):
    return render(request, 'speakers/event.html')