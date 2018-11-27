# Import for BreakBeam
import RPi.GPIO as GPIO
# Import for Magnetometer
from past import autotranslate
autotranslate(['FaBo9Axis_MPU9250'])
import FaBo9Axis_MPU9250
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
        self.sensor = FaBo9Axis_MPU9250.MPU9250()

    def poll(self):
        """
        Polls the magnetometer
        :return: the average magnetometer value on the x, y, and z axes
        """
        mag = self.sensor.readMagnet()
        return (mag['x'] + mag['y'] + mag['z']) / 3


class ProximitySensor:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_vcnl4010.VCNL4010(self.i2c)

    def poll(self):
        """
        Polls the proximity sensor
        :return: the raw proximity value
        """
        return self.sensor.proximity

    @staticmethod
    def min_distance():
        """
        Returns the set value which represents a distance of 0
        :return: the set value which represents a distance of 0
        """
        return 65535
