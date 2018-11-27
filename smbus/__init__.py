import sys
# Essentially, create an alias of smbus2 to smbus
import smbus2
sys.modules[__name__] = sys.modules['smbus2']