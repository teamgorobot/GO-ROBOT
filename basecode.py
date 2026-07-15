# Imports
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Light, Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import vector, wait, StopWatch

# Debug Level:
# 0 = no messages
# 1 = standard Debug messages
# 2 = more detailed Debug messages
# 3 = all Debug messages
debug = 1

# Hub definition
hub = PrimeHub(top_side=-Axis.X, front_side=Axis.Y) # type: ignore
if debug == 3:
    print("Hub defined successfully")

# Motor definition
drive_motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
drive_motor_right = Motor(Port.E)
normal_motor_left = Motor(Port.C)
normal_motor_right = Motor(Port.F)
if debug == 3:
    print("Motors defined successfully")

# Color Sensor definition
color_sensor_left = ColorSensor(Port.B)
color_sensor_right = ColorSensor(Port.D)
if debug == 3:
    print("Color sensors defined successfully")

# Direction definition
class direction:
    left = None
    right = None
if debug == 3:
    print("Directions defined successfully")

# Button definition
class button:
    middle = Button.CENTER
    left = Button.LEFT
    right = Button.RIGHT
    bluetooth = Button.BLUETOOTH
if debug == 3:
    print("Buttons defined successfully")

# DriveBase definition
drivebase = DriveBase(drive_motor_left, drive_motor_right, 47, 120)
if debug == 3:
    print("DriveBase defined successfully")

# Gyro driving definition
drivebase.use_gyro(True)
if debug == 3:
    print("Gyro enabled successfully")

# Loop variable definition
lightBlink = False
loop = False
if debug == 3:
    print("Loop variables defined successfully")
if debug >= 2:
    print("Variable initialization complete")

# Motor def definition
def driveinf(speed=100, degrees_per_sec=0):
    drivebase.drive(speed, degrees_per_sec)
if debug == 3:
    print("Drive infinite function defined successfully")
def turn(direction, degrees):
    if direction == "left":
        degrees = -degrees
    elif direction == "right":
        degrees = degrees
    drivebase.turn(degrees)
if debug == 3:
    print("Turn function defined successfully")
def straight(length):
        length = length * 4.9
        drivebase.straight(length)
if debug == 3:
    print("Drive straight function defined successfully")
if debug == 3:
    print("Drive functions defined successfully")

# Speed definition
drive_motor_left.control.limits(2000, 2000, 100)
drive_motor_right.control.limits(2000, 2000, 100)
drivebase.settings(200, 200, 100, 100)
class speed:
    @staticmethod
    def fast():
        drivebase.settings(400, 400, 200, 200)
    @staticmethod
    def slow():
        drivebase.settings(200, 200, 100, 100)
if debug >= 2:
    print("Motor settings set successfully")

def checkcolor(sensor=color_sensor_left, untilcolor=False,):
    wait(500)
    if untilcolor:
        for _ in range(50):
            color = sensor.color(surface=True)
            if color != Color.NONE:
                print(color)
                return color
            wait(50)
        print("No color detected")
        return Color.NONE
    else:
        color = sensor.color(surface=True)
        print(color)
        return color
if debug >= 2:
    print("Check color function defined successfully")

# UI definition
def BatteryUI():
    battery_voltage = hub.battery.voltage()

    max_voltage = 12.6  # Max voltage when fully charged in volts
    min_voltage = 9.0   # Approximate safe minimum voltage

    battery_percentage = (battery_voltage - min_voltage) / (max_voltage - min_voltage) * 100
    battery_percentage = max(0, min(100, battery_percentage))  # Clamp value between 0 and 100
    print(f"{battery_percentage:.1f}% Power")
    if battery_percentage <= 20:
        hub.display.pixel(4, 0, 50)
    elif battery_percentage <= 40:
        hub.display.pixel(4, 0, 50)
        hub.display.pixel(4, 1, 50)
    elif battery_percentage <= 60:
        hub.display.pixel(4, 0, 50)
        hub.display.pixel(4, 1, 50)
        hub.display.pixel(4, 2, 50)
    elif battery_percentage <= 80:
        hub.display.pixel(4, 0, 50)
        hub.display.pixel(4, 1, 50)
        hub.display.pixel(4, 2, 50)
        hub.display.pixel(4, 3, 50)
    elif battery_percentage <= 100:
        hub.display.pixel(4, 0, 50)
        hub.display.pixel(4, 1, 50)
        hub.display.pixel(4, 2, 50)
        hub.display.pixel(4, 3, 50)
        hub.display.pixel(4, 4, 50)
if debug >= 2:
    print("Battery UI function defined successfully")

# Loop definition
def toggleLoop():
    global lightBlink, loop
    if lightBlink:
        hub.light.on(Color.RED)
        lightBlink = False
        loop = False
    elif lightBlink == False:
        hub.light.blink(Color.YELLOW, (500, 500))
        lightBlink = True
        loop = True
if debug >= 2:
    print("Toggle loop function defined successfully")

# Wait until Button pressed definition
def waituntilbutton(button):
    if debug >= 1:
        print("Waiting for button press...")
    while button not in hub.buttons.pressed():
        wait(2)
    if debug == 3:
        print("Middle button pressed, proceeding with program")
if debug == 3:
    print("Wait until button function defined successfully")

# Startup definition
if debug >= 1:
    print("Program started successfully")
def startup():
    BatteryUI()
    hub.system.set_stop_button(button.bluetooth)
    hub.light.on(Color.RED)
    waituntilbutton(button.middle)

# Run definition
def run():
    # The Run
    if debug >= 1:
        print("Button pressed, Run started successfully")
    hub.light.on(Color.GREEN)
    hub.display.icon(Icon.ARROW_UP)

    # Code here
















    if debug >= 1:
        print("Run ended successfully")

if not loop:
    startup()
    run()
else:
    while True:
        startup()
        run()

if debug >= 1:
    print("Program ended successfully")
