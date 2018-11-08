from django.shortcuts import render
from .models import *
from datetime import datetime, timedelta
from . import timeanddate
from tzlocal import get_localzone
from dateutil.relativedelta import relativedelta


# Create your views here.
def livedata(request):
    return render(request, "data/livedata.json")


def statistics(request, years, months, days, hours, minutes):
    cutoff = datetime.now() - relativedelta(years=int(years), months=int(months), days=int(days), hours=int(hours), minutes=int(minutes))
    breakbeam = BreakBeam.objects.filter(event__gte=cutoff)
    magnetometer = Magnetometer.objects.filter(measured_at__gte=cutoff)
    proximity = Proximity.objects.filter(measured_at__gte=cutoff)
    context = {
        'cutoff_year': str(cutoff.year),
        'cutoff_month': str(cutoff.month),
        'cutoff_day': str(cutoff.day),
        'cutoff_hour': str(cutoff.hour),
        'cutoff_minute': str(cutoff.minute),
        'num_breakbeam': len(breakbeam),
        'magnetometer': magnetometer,
        'proximity': proximity
    }

    return render(request, "data/statistics.json", context=context)