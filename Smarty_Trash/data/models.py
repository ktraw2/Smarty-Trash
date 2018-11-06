from django.db import models


# Create your models here.
class BreakBeam(models.Model):
    event = models.DateTimeField()


class Magnetometer(models.Model):
    measured_at = models.DateTimeField()
    value = models.FloatField()


class Proximity(models.Model):
    measured_at = models.DateTimeField()
    value = models.FloatField()
