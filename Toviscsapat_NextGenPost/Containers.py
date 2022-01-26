#!/usr/bin/env pybricks-micropython
from MyBlocks import Drive, MedMotor, NoGyroTU, AbsTU, AbsDRV, Align, LFOL
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

gyro = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)
gyro.reset_angle(0)

# Start
def First():
    # AbsTU(30, 100, gyro)
    # wait(1000)
    # AbsDRV(30, 100, 65, gyro)
    # wait(1000)
    # AbsTU(90, 100, gyro)
    # wait(1000)
    # AbsDRV(90, 100, 120, gyro)
    # wait(1000)
    # AbsTU(180, 100, gyro)
    # wait(1000)
    # AbsDRV(180, 100, 25, gyro)
    # wait(1000)
    # AbsTU(270, 100, gyro)
    AbsDRV(30, 100, 15, gyro)
    LFOL(color1, color2, 70, 130, 1, 4)
    wait(1000)
    MedMotor(-50, 50, "D", [1, 1])
    wait(1000)
    MedMotor(50, 50, "D", [9, 9])
    wait(1000)
    AbsTU(180, 100, gyro)
    wait(1000)
    MedMotor(-10, 100, "A", [1, 1])
    wait(1000)
    AbsDRV(180, 100, -25, gyro)
    wait(1000)
    AbsTU(270, 100, gyro)
    wait(1000)
    AbsDRV(270, 100, 200, gyro)
    wait(1000)
# End
