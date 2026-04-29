# Good luck finding out who alex is

# Imports
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Light, Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import vector, wait, StopWatch

# Set to 0 for no debug messages, 1 for standard Debug messages, 2 for more detailed Debug messages, or 3 for all Debug messages
debug = 1

# Hub
hub = PrimeHub(top_side=Axis.Y, front_side=Axis.Z)  # type: ignore
if debug == 3:
    print("Hub defined successfully")

# Sensors
colorsensor = ColorSensor(Port.C)
if debug == 3:
    print("Sensors defined successfully")

# Directions
left = "left"
right = "right"

# Motors
m1 = Motor(Port.F, Direction.COUNTERCLOCKWISE)
m2 = Motor(Port.E)
grabm = Motor(Port.A)
arm = Motor(Port.D, Direction.COUNTERCLOCKWISE)
if debug == 3:
    print("Motors defined successfully")

# Buttons
class button:
    middle = Button.CENTER
    left = Button.LEFT
    right = Button.RIGHT
    bluetooth = Button.BLUETOOTH

if debug == 3:
    print("Buttons defined successfully")
# DriveBases
drivebase = DriveBase(m1, m2, 56, 95)
if debug == 3:
    print("DriveBase defined successfully")

# Motor Variables
grabbing = False

# Loop variables
lightBlink = False
loop = False
if debug == 3:
    print("Loop variables defined successfully")
if debug >= 2:
    print("Variable initialization complete")
# Optional for better driving
drivebase.use_gyro(True)
if debug == 3:
    print("Gyro enabled successfully")

# Definitions for Motors
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
def turnarm(degrees):
        arm.run_angle(1000, -degrees, Stop.HOLD)
if debug == 3:
    print("Turn arm function defined successfully")
def grab():
        global grabbing
        if grabbing:
            grabm.run_angle(1000, 75, Stop.HOLD, False)
            wait(500)
            grabbing = False
        elif grabbing == False:
            grabm.run_angle(1000, -75, Stop.HOLD, False)
            wait(500)
            grabbing = True
if debug == 3:
    print("Grab function defined successfully")
if debug == 3:
    print("Arm functions defined successfully")
if debug >= 2:
    print("Motor functions defined successfully")

# Making the motors faster
m1.control.limits(2000, 2000, 200)
m2.control.limits(2000, 2000, 200)
drivebase.settings(200, 200, 100, 100)
def fast():
    drivebase.settings(400, 400, 200, 200)
def slow():
    drivebase.settings(200, 200, 100, 100)
if debug >= 2:
    print("Motor settings set successfully")

# Check color
def checkcolor(untilcolor=False):
    wait(500)
    if untilcolor:
        for _ in range(50):
            color = colorsensor.color(surface=True)
            if color != Color.NONE:
                print(color)
                return color
            wait(50)
        print("No color detected")
        return Color.NONE
    else:
        color = colorsensor.color(surface=True)
        print(color)
        return color
if debug >= 2:
    print("Check color function defined successfully")

# UI
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

# Wait until Button pressed
def waituntilbutton(button):
    if debug >= 1:
        print("Waiting for button press...")
    while button not in hub.buttons.pressed():
        wait(2)
    if debug == 3:
        print("Middle button pressed, proceeding with program")
if debug == 3:
    print("Wait until button function defined successfully")

# Startup
if debug >= 1:
    print("Program started successfully")
def startup():
    BatteryUI()
    hub.system.set_stop_button(button.bluetooth)
    hub.light.on(Color.RED)
    waituntilbutton(button.middle)

def run():
    # The Run
    if debug >= 1:
        print("Button pressed, Run started successfully")
    hub.light.on(Color.GREEN)
    hub.display.icon(Icon.ARROW_UP)

    # Code here
    # getting alex
    straight(50)
    turn(left, 90)
    straight(50)
    turn(right, 90)
    straight(38)
    grab()
    straight(-140)
    turn(left, 90)
    # driving to mud area
    fast()
    straight(345)
    slow()
    turn(left, 90)
    straight(25)
    # pushing mud bricks away
    # row 1
    turnarm(90)
    fast()
    straight(-130)
    turnarm(-90)
    straight(130)
    slow()
    turn(left, 90)
    straight(35)
    turn(right, 90)
    # row 2
    turnarm(90)
    fast()
    straight(-85)
    straight(10)
    turnarm(-90)
    straight(40)
    slow()
    # putting away alex
    turn(right, 50)
    straight(20)
    grab()
    straight(-15)
    turn(left, 55)
    straight(-15)
    turn(left, 90)
    # driving to get blue figure
    fast()
    straight(345)
    slow()
    turn(left, 90)
    straight(90)
    grab()
    straight(-100)
    turn(left, 90)
    # driving to mud area to put away blue figure
    fast()
    straight(373)
    slow()
    turn(right, 90)
    straight(70)
    grab()
    straight(-55)
    turn(left, 90)
    # driving to random artefacts
    fast()
    straight(-160)
    slow()
    turn(right, 90)
    straight(105)
    # Slot 1
    grab()
    color = checkcolor(True)
    if color == Color.BLUE:
        turn(right, 180)
        fast()
        straight(175)
        slow()
        turn(left, 90)
        straight(15)
        turn(right, 90)
        straight(20)
        grab()
    elif color == Color.RED:
        turn(right, 180)
        fast()
        straight(175)
        slow()
        turn(left, 90)
        straight(120)
        turn(right, 90)
        straight(23)
        grab()
    elif color == Color.GREEN:
        turn(right, 180)
        fast()
        straight(175)
        slow()
        turn(left, 90)
        straight(60)
        turn(right, 90)
        straight(53)
        grab()
    elif color == Color.YELLOW:
        turn(right, 180)
        fast()
        straight(175)
        slow()
        turn(left, 90)
        straight(73)
        turn(right, 90)
        straight(23)
        grab()
    elif color == Color.BLACK:
        turn(right, 180)
        fast()
        straight(175)
        slow()
        turn(left, 90)
        straight(-33)
        turn(right, 90)
        straight(30)
    



    if debug >= 1:
        print("Run ended successfully")

if loop:
    while True:
        startup()
        run()
elif loop == False:
    startup()
    run()
else:
    if debug >= 2:
        print("Error: loop variable is not a boolean")

if debug >= 1:
    print("Program ended successfully")

# Tutorial:
# driveinf(speed=100, degrees_per_sec): drive infinitely with speed(standard 100), degrees_per_sec(standard 0)
# straight(length): drive straight for length in mm
# turn(degrees): turn for desired degrees
# turnarm(degrees): turn arm for desired 
# grab(): grab or release object
# checkcolor(True/False) check color of color sensor, if True check repeatedly for 5 seconds
# button.buttonname: button variables
# debug = ...: Change for debug log level