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
normal_motor_left = Motor(Port.B)
normal_motor_right = Motor(Port.C)
if debug == 3:
    print("Motors defined successfully")

# Color Sensor definition
color_sensor_left = ColorSensor(Port.D)
color_sensor_right = ColorSensor(Port.F)
if debug == 3:
    print("Color sensors defined successfully")

# Direction definition
class direction:
    left = object()
    right = object()
if debug == 3:
    print("Directions defined successfully")

# Button definition
class button:
    middle = Button.CENTER
    left = Button.LEFT
    right = Button.RIGHT
    bluetooth = Button.BLUETOOTH
start = button.middle
if debug == 3:
    print("Buttons defined successfully")


def button_beep():
    hub.speaker.beep(1000, 100)

def action_beep():
    hub.speaker.beep(600, 50)

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
class RunStopped(Exception):
    pass

def check_run_stop():
    if start in hub.buttons.pressed():
        button_beep()
        drivebase.stop()
        normal_motor_left.stop()
        normal_motor_right.stop()
        raise RunStopped

def driveinf(speed=100, degrees_per_sec=0):
    check_run_stop()
    action_beep()
    drivebase.drive(speed, degrees_per_sec)
if debug == 3:
    print("Drive infinite function defined successfully")
def turn(turn_direction, degrees):
    if turn_direction is direction.left:
        degrees = -degrees
    elif turn_direction is direction.right:
        degrees = degrees
    else:
        raise ValueError("turn direction must be direction.left or direction.right")
    while abs(degrees) > 0:
        check_run_stop()
        turn_step = 5 if degrees > 0 else -5
        if abs(degrees) < 5:
            turn_step = degrees
        action_beep()
        drivebase.turn(turn_step)
        degrees -= turn_step
if debug == 3:
    print("Turn function defined successfully")
def straight(length):
    length *= 4.9
    while abs(length) > 0:
        check_run_stop()
        straight_step = 10 if length > 0 else -10
        if abs(length) < 10:
            straight_step = length
        action_beep()
        drivebase.straight(straight_step)
        length -= straight_step
if debug == 3:
    print("Drive straight function defined successfully")
if debug == 3:
    print("Drive functions defined successfully")
def move(move_direction, degrees, speed=100):
    if move_direction is direction.left:
        motor = normal_motor_left
    elif move_direction is direction.right:
        motor = normal_motor_right
    else:
        raise ValueError("move direction must be direction.left or direction.right")

    while abs(degrees) > 0:
        check_run_stop()
        move_step = 10 if degrees > 0 else -10
        if abs(degrees) < 10:
            move_step = degrees
        action_beep()
        motor.run_angle(speed, move_step)
        degrees -= move_step


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
    def set(speed=200):
        speed2 = speed / 2
        drivebase.settings(speed, speed, speed2, speed2)
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
def display_battery(battery_percentage):
    battery_pixels = int((battery_percentage + 19) // 20)
    for y in range(battery_pixels):
        hub.display.pixel(4, y, 50)

def BatteryUI():
    battery_voltage = hub.battery.voltage()

    max_voltage = 12.6  # Max voltage when fully charged in volts
    min_voltage = 9.0   # Approximate safe minimum voltage

    battery_percentage = (battery_voltage - min_voltage) / (max_voltage - min_voltage) * 100
    battery_percentage = max(0, min(100, battery_percentage))  # Clamp value between 0 and 100
    print(f"{battery_percentage:.1f}% Power")
    display_battery(battery_percentage)
if debug >= 2:
    print("Battery UI function defined successfully")

# Run Menu
def display_run(run):
    digits = {
        1: ("111", "010", "010", "110", "010"),
        2: ("111", "100", "010", "001", "110"),
        3: ("110", "001", "010", "001", "110"),
    }
    hub.display.off()
    for y, row in enumerate(digits[run]):
        for x, pixel in enumerate(row, 1):
            if pixel == "1":
                hub.display.pixel(x, y, 100)
    battery_voltage = hub.battery.voltage()
    battery_percentage = (battery_voltage - 9.0) / (12.6 - 9.0) * 100
    battery_percentage = max(0, min(100, battery_percentage))
    display_battery(battery_percentage)

def runmenu(left, right, start, initial_run=1):
    if debug >= 1:
        print("Choose Run")
    run = initial_run
    display_run(run)
    print("Run {} selected".format(run))
    while True:
        pressed = hub.buttons.pressed()
        if left in pressed:
            button_beep()
            run = 3 if run == 1 else run - 1
            display_run(run)
            print("Run {} selected".format(run))
            wait(300)
        elif right in pressed:
            button_beep()
            run = 1 if run == 3 else run + 1
            display_run(run)
            print("Run {} selected".format(run))
            wait(300)
        elif start in pressed:
            button_beep()
            print("Executing Run {}".format(run))
            wait(300)
            return run
        wait(50)
if debug == 3:
    print("Run Menu function defined successfully")

# Startup definition
if debug >= 1:
    print("Program started successfully")
def startup(initial_run=1):
    BatteryUI()
    wait(3)
    hub.system.set_stop_button(button.bluetooth)
    hub.light.on(Color.RED)
    return runmenu(button.left, button.right, start, initial_run)

# Run definitions
def run1():
    if debug >= 1:
        print("Run 1 started successfully")
    hub.light.on(Color.GREEN)
    hub.display.icon(Icon.ARROW_UP)

    # Code here

    straight(100)














    if debug >= 1:
        print("Run 1 ended successfully")

def run2():
    if debug >= 1:
        print("Run 2 started successfully")
    hub.light.on(Color.GREEN)

    # Code for Run 2 here

    if debug >= 1:
        print("Run 2 ended successfully")

def run3():
    if debug >= 1:
        print("Run 3 started successfully")
    hub.light.on(Color.GREEN)

    # Code for Run 3 here

    if debug >= 1:
        print("Run 3 ended successfully")

next_run = 1
while True:
    selected_run = startup(next_run)
    cancelled = False
    try:
        if selected_run == 1:
            run1()
        elif selected_run == 2:
            run2()
        elif selected_run == 3:
            run3()
    except RunStopped:
        cancelled = True
        if debug >= 1:
            print("Run stopped; returning to menu")
    if cancelled:
        next_run = selected_run
    else:
        next_run = 1 if selected_run == 3 else selected_run + 1

if debug >= 1:
    print("Program ended successfully")
