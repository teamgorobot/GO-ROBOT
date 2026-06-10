from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Light, Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import vector, wait, StopWatch

# Set to 0 for no debug messages, 1 for standard Debug messages, 2 for more detailed Debug messages, or 3 for all Debug messages
debug = 1

hub = PrimeHub()
if debug == 3:
    print("Hub defined successfully")
