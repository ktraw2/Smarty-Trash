# Create your tasks here
# Imports for Celery
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task
# Imports for sensors
from .sensors import *
import time
from .models import *
from datetime import datetime


@periodic_task(
    run_every=(crontab(minute="*/1")),
    name="poll_breakbeam",
    ignore_result=True
)
def poll_breakbeam():
    breakbeam = BreakBeamSensor()
    while False:
        if breakbeam.poll():
            entry = BreakBeam(event=datetime.now())
            entry.save()
        time.sleep(0.01)


@periodic_task(
    run_every=(crontab(minute="*/1")),
    name="poll_magnetometer",
    ignore_result=True
)
def poll_magnetometer():
    magnetometer = MagnetometerSensor()
    value = magnetometer.poll()
    if value > magnetometer.threshold:
        entry = Magnetometer(measured_at=datetime.now(), value=value)
        entry.save()


@periodic_task(
    run_every=(crontab(minute="*/1")),
    name="poll_proximity",
    ignore_result=True
)
def poll_proximity():
    proximity = ProximitySensor()
    value = proximity.poll()
    if value > proximity.threshold:
        entry = Proximity(measured_at=datetime.now(), value=value)
        entry.save()
