from django.shortcuts import render
from django.utils import timezone
from datetime import datetime


def partners(request):
    return render(request, 'partners/partners.html')

def about_us(request):
    return render(request, 'about_us/about_us.html')

def contact(request):
    return render(request, 'speakers/contact.html')

