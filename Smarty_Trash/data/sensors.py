# Imports for BreakBeam
import RPi.GPIO as GPIO
# Imports for Magnetometer
from machine import Pin
from machine import I2C as Machine_I2C
from FaBo9Axis_MPU9250 import MPU9250
# Imports for Proximity
import board
import busio
import adafruit_vcnl4010


class BreakBeamSensor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.IN)

    def poll(self):
        """
        Polls the IR Break Beam sensor
        :return: whether or not the beam was broken
        """
        if GPIO.input(17) == 1:
            return True
        if GPIO.input(17) == 0:
            return False


class MagnetometerSensor:
    def __init__(self):
        self.threshold = 47
        self.i2c = Machine_I2C(scl=Pin(22), sda=Pin(21))
        self.sensor = MPU9250(self.i2c)
        print("MPU9250 id: " + hex(self.sensor.whoami))

    def poll(self):
        return self.sensor.magnetic


class ProximitySensor:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_vcnl4010.VCNL4010(i2c)

    def poll(self):
        return self.sensor.proximity

    @staticmethod
    def min_distance():
        return 65535
