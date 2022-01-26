#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
BMotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, gears=none)
CMotor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE, gears=none)
Speed = speed
DRV = DriveBase(BMotor, CMotor, 81.6, 105)
CM = cm
Steering = steering
TargetRot = CM/(8.16*3.1416)


# Write your program here.
def Drive(speed, cm, steering):
    BMotor.reset_angle(0)
    CMotor.reset_angle(0)
    while ((BMotor.angle() + CMotor.angle())/2 < TargetRot):
        DRV.drive(Speed, Steering)
    DRV.stop()