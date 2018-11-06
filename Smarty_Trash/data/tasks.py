# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
# import RPi.GPIO as GPIO

# @shared_task
# def monitor_break_beam():
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setup(17, GPIO.IN)
#     while True:
#         if (GPIO.input(17) == 1):
#             print("Beam Broken")
#         if (GPIO.input(17) == 0):
#             print("Solid")


@shared_task()
def poll_magnetometer():
    pass


@shared_task()
def poll_proximity():
    pass

@shared_task()
def add(x, y):
    return x + y
