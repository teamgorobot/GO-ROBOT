# Imports
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Light, Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Hub
hub = PrimeHub()

# Sensors
colorsensor = ColorSensor(Port.D)

# Motors
m1 = Motor(Port.A, Direction.COUNTERCLOCKWISE)
m2 = Motor(Port.B)
grabm = Motor(Port.E)
arm = Motor(Port.C, Direction.COUNTERCLOCKWISE)

# Buttons
middlebutton = Button.CENTER
bluetoothbutton = Button.BLUETOOTH

# DriveBases
drive = DriveBase(m1, m2, 56, 95)

# Optional for better driving
drive.use_gyro(True)

# Definitions for Motors
def driveinf(speed=100, degrees_per_sec=0):
    drive.drive(speed, degrees_per_sec)
def turn(degrees):
    drive.turn(degrees)
def straight(length):
    drive.straight(length)
def turnarm(degrees):
    arm.run_angle(1000, degrees, Stop.HOLD, False)
def grab(grab):
    if grab:
        grabm.run_angle(1000, -55, Stop.HOLD, False)
    elif grab == False:
        grabm.run_angle(1000, 55, Stop.HOLD, False)

# check color
def checkcolor(untilcolor=False):
    if untilcolor == True:
        while colorsensor.color(surface=True) == Color.NONE:
            wait(50)
        color = colorsensor.color(surface=True)
        print(color)
        return color
    elif untilcolor == False:
        color = colorsensor.color(surface=True)
        print(color)
        return color

# Startup
print("Program started successfully")
hub.system.set_stop_button(bluetoothbutton)
hub.light.on(Color.RED)

# The Run
print("Run started successfully")
hub.light.on(Color.GREEN)
hub.display.icon(Icon.HAPPY)

# Code here
turn(90)

