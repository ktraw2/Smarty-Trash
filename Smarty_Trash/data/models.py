from django.db import models


# Create your models here.
class BreakBeam(models.Model):
    event = models.DateTimeField()

    def __str__(self):
        return "Break Beam Data"

    class Meta:
        verbose_name_plural = "Break Beam Data"


class Magnetometer(models.Model):
    measured_at = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return "Magnetometer Data"

    class Meta:
        verbose_name_plural = "Magnetometer Data"


class Proximity(models.Model):
    measured_at = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return "Proximity Data"

    class Meta:
        verbose_name_plural = "Proximity Data"
