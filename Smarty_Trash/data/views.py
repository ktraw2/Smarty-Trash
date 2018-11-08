from django.shortcuts import render
from .models import *
from datetime import datetime
from dateutil.relativedelta import relativedelta
DEBUG = True
if not DEBUG:
    from .sensors import *


# Create your views here.
def live(request):
    if not DEBUG:
        magnetometer = MagnetometerSensor()
        magnetometer_value = magnetometer.poll()
        if magnetometer_value > magnetometer.threshold:
            entry = Magnetometer(measured_at=datetime.now(), value=magnetometer_value)
            entry.save()
        proximity = ProximitySensor()
        proximity_value = proximity.poll()
        if proximity_value > proximity.threshold:
            entry = Proximity(measured_at=datetime.now(), value=proximity_value)
            entry.save()
        context = {
            'magnetometer_value': magnetometer_value,
            'magnetometer_threshold': magnetometer.threshold,
            'proximity_value': proximity_value,
            'proximity_threshold': proximity.threshold
        }
    else:
        context = {
            'magnetometer_value': -1,
            'magnetometer_threshold': 0,
            'proximity_value': -1,
            'proximity_threshold': 0
        }
    return render(request, "data/livedata.json", context)


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