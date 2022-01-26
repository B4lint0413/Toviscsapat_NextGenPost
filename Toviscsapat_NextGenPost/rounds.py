#!/usr/bin/env pybricks-micropython
from MyBlocks import Drive, MedMotor, NoGyroTU, AbsTU, AbsDRV, Align, LFOL
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
# from multiprocessing import Process
import time

ev3 = EV3Brick()

# def StopRound():
#     while True:
#         if ev3.buttons.pressed() == Button.CENTER:
#             p1.
#             break
gyro = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)
color1 = ColorSensor(Port.S2)
color2 = ColorSensor(Port.S3)
AMotor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
BMotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
CMotor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
DMotor = Motor(Port.D, positive_direction=Direction.CLOCKWISE)
# isRunning = True

def Round(nth):
    # isRunning = True
    if nth == 1:
        print("First round")
        # time.sleep(10)
        AbsTU(30, 10, gyro)
        wait(1000)
        AbsDRV(10, 10, 65, gyro)
        wait(1000)
        AbsTU(90, 10, gyro)
        wait(1000)
        AbsDRV(10, 10, 120, gyro)
        wait(1000)
        AbsTU(180, 10, gyro)
        wait(1000)
        AbsDRV(10, 10, 25, gyro)
        wait(1000)
        AbsTU(270, 10, gyro)
        wait(1000)
        MedMotor(-50, 50, DMotor, gyro, [10])
        wait(1000)
        MedMotor(50, 50, DMotor, gyro, [90])
        wait(1000)
        AbsTU(180, 10, gyro)
        wait(1000)
        MedMotor(-10, 10, AMotor, gyro, [1])
        wait(1000)
        AbsDRV(10, 10, -25, gyro)
        wait(1000)
        AbsTU(270, 10, gyro)
        wait(1000)
        AbsDRV(10, 10, 200, gyro)
        wait(1000)
    elif nth == 2:
        print("Second round")
        # time.sleep(10)
        AbsDRV(0, 50, 15, gyro)
        wait(1000)
        #LFOL 177cm
        LFOL(color1, color2, 80, 80, 1.3, 5)
        wait(500)
        MedMotor(100, 167, AMotor, [1.67, 1])
        wait(500)
        LFOL(color1, color2, 80, 60, 1.3, 5)
        wait(500)
        MedMotor(100, 105, AMotor, [1.67, 1])
        wait(500)
        LFOL(color1, color2, 80, 50, 1.3, 5)
        wait(500)
        MedMotor(100, 180, DMotor, [1, 1])
        wait(500)
        LFOL(color1, color2, 80, 20, 1.3, 5)
    elif nth == 3:
        print("Second round")
        # time.sleep(10)
        wait(1000)
        MedMotor(200, 90, AMotor, [12, 22])
        Drive(200, 64, 0)
        wait(1000)
        NoGyroTU(-200, 55)
        wait(1000)
        MedMotor(200, 150, DMotor, [12, 20])
        wait(1000)
        MedMotor(-200, 80, DMotor, [12, 20])
        wait(1000)
        NoGyroTU(200, 130)
        wait(1000)
        MedMotor(200, 80, DMotor, [12, 20])
        wait(1000)
        Drive(200, 15, 0)
        wait(1000)
        MedMotor(-200, 60, DMotor, [12, 20])
        End()

from main import Running
def End():
    Running(False)
#     isRunning = False
#     return isRunning
# def stop():
#     time.sleep(1)
#     while isRunning:
#         if Button.CENTER in ev3.buttons.pressed():
#             print("Stop")
#             return Round