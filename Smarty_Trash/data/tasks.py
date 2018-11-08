# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .sensors import *
import time
from .models import *
from datetime import datetime


@shared_task()
def poll_breakbeam():
    breakbeam = BreakBeamSensor()
    while True:
        if breakbeam.poll():
            entry = BreakBeam(event=datetime.now())
            entry.save()
        time.sleep(0.01)


@shared_task()
def poll_magnetometer():
    magnetometer = MagnetometerSensor()
    value = magnetometer.poll()
    if value > magnetometer.threshold:
        entry = Magnetometer(measured_at=datetime.now(), value=value)
        entry.save()


@shared_task()
def poll_proximity():
    proximity = ProximitySensor()
    value = proximity.poll()
    if value > proximity.threshold:
        entry = Proximity(measured_at=datetime.now(), value=value)
        entry.save()
