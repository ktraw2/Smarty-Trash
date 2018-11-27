from Smarty_Trash.data.sensors import *
import time

breakbeam = BreakBeamSensor()
magnetometer = MagnetometerSensor()
proximity = ProximitySensor()

while True:
    print("-----Sensor Values-----")
    print("Break Beam: " + str(breakbeam.poll()))
    print("Magnetometer: " + str(magnetometer.poll()))
    print("Proximity: " + str(proximity.poll()))
    time.sleep(1)
