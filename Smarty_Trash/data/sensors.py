# Imports for BreakBeam
import RPi.GPIO as GPIO
# Imports for Magnetometer
from machine import Pin
from machine import I2C as Machine_I2C
from FaBo9Axis_MPU9250 import MPU9250
# Imports for Proximity
import time
from Adafruit_GPIO import I2C as Adafruit_I2C


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
    def __init__(self, address=0x13):
        self.threshold = 0
        self.VCNL4000_ADDRESS = 0x13

        # Commands
        self.VCNL4000_COMMAND = 0x80
        self.VCNL4000_PRODUCTID = 0x81
        self.VCNL4000_IRLED = 0x83
        self.VCNL4000_AMBIENTPARAMETER = 0x84
        self.VCNL4000_AMBIENTDATA = 0x85
        self.VCNL4000_PROXIMITYDATA = 0x87
        self.VCNL4000_SIGNALFREQ = 0x89
        self.VCNL4000_PROXINITYADJUST = 0x8A

        self.VCNL4000_3M125 = 0
        self.VCNL4000_1M5625 = 1
        self.VCNL4000_781K25 = 2
        self.VCNL4000_390K625 = 3

        self.VCNL4000_MEASUREAMBIENT = 0x10
        self.VCNL4000_MEASUREPROXIMITY = 0x08
        self.VCNL4000_AMBIENTREADY = 0x40
        self.VCNL4000_PROXIMITYREADY = 0x20

        self.i2c = Adafruit_I2C.Device(address, 0)
        self.address = address
        # Write proximity adjustement register
        self.i2c.write8(self.VCNL4000_PROXINITYADJUST, 0x81)

    def poll(self):
        self.i2c.write8(self.VCNL4000_COMMAND, self.VCNL4000_MEASUREPROXIMITY)
        result = self.i2c.readU8(self.VCNL4000_COMMAND)
        # Wait until the sensor is ready
        while not (result and self.VCNL4000_PROXIMITYREADY):
            time.sleep(0.001)
        return self.i2c.readU16(self.VCNL4000_PROXIMITYDATA)
