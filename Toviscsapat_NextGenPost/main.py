#!/usr/bin/env pybricks-micropython
from MyBlocks import Drive, MedMotor, NoGyroTU, AbsTU, AbsDRV, Align, LFOL
from Containers import First
import multiprocessing
from multiprocessing import Process
from time import sleep
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image, Font
# import ToCM


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Declare the sensors and motors, and reset them (we reset them just here, and it has a reason).
ev3 = EV3Brick()
gyro = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)
gyro.reset_angle(0)
color1 = ColorSensor(Port.S2)
color2 = ColorSensor(Port.S3)
AMotor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
BMotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
CMotor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
DMotor = Motor(Port.D, positive_direction=Direction.CLOCKWISE)

isRunning = False

def Running(Runs):
    global isRunning
    isRunning = Runs

#The actual rounds
def Round(nth):
    if nth == 1:
        print("First round")
        MedMotor(-200, 120, "D", [8, 18])
        AbsDRV(30, 100, 25, gyro)
        LFOL(color1, color2, 70, 100, 1, 4)
        LFOL(color1, color2, 70, 40, 0.7, 3)
        wait(1500)
        print(gyro.angle())
        AbsTU(183, 100, gyro)
        MedMotor(100, 50, "A", [1, 2])
        AbsDRV(183, 200, 48, gyro)
        wait(2000)
        MedMotor(-100, 42, "A", [1, 2])
        AbsDRV(180, -100, -35, gyro)
        AbsTU(90, 100, gyro)
        AbsDRV(75, -100, -255, gyro)
   elif nth == 2:
        print("Second round")
        AbsDRV(0, 50, 15, gyro)
        wait(1000)
        #LFOL 177cm
        LFOL(color1, color2, 80, 80, 1.3, 5)
        wait(500)
        MedMotor(100, 167, "A", [1.67, 1])
        wait(500)
        LFOL(color1, color2, 80, 60, 1.3, 5)
        wait(500)
        MedMotor(100, 105, "A", [1.67, 1])
        wait(500)
        LFOL(color1, color2, 80, 50, 1.3, 5)
        wait(500)
        MedMotor(100, 180, "D", [1, 1])
        wait(500)
        LFOL(color1, color2, 80, 20, 1.3, 5)
    elif nth == 3:
        print("Third round")
        AbsDRV(0, 100, 20, gyro)
        LFOL(color1, color2, 100, 50, 1.3, 3)
        Align(color1, color2)
        MedMotor(130, 200, "D", [1, 1.2])
        wait(1000)
        MedMotor(-130, 200, "D", [1, 1.2])
        MedMotor(130, 200, "A", [1, 1.2])
        AbsDRV(60, 100, 13, gyro)
        MedMotor(-130, 100, "A", [1, 1.2])
        MedMotor(130, 80, "A", [1, 1.2])
        AbsDRV(45, -150, -20, gyro)
        AbsDRV(45, -200, -50, gyro)
    Running(False)

#Setting up the display
curRound = 1
Rounds = ["Containers", "Tower", "Airplane", "Last"]
screen = Image("Screen", sub=False)
font = Font(family=None, size=14)
ev3.screen.set_font(font)

#Setting up the text file
text = open("CurrentRound.txt", "r")
txt = text.readlines()
print(txt)
print(len(txt))
curRound = int(txt[len(txt)-1].replace("\n", ""))
text.close()
Text = open("CurrentRound.txt", "w")

#The (infinite) main loop
while True:
    Text.write(str(curRound)+"\n")
    sleep(0.3)
    
    #Center button
    if Button.CENTER in ev3.buttons.pressed() and not isRunning:
        gyro.reset_angle(0)
        AMotor.reset_angle(0)
        BMotor.reset_angle(0)
        CMotor.reset_angle(0)
        DMotor.reset_angle(0)
        ev3.speaker.play_file(SoundFile.READY)
        Round(curRound)
        sleep(0.5)
        if curRound < 4:
            curRound += 1

    #Upper button
    elif Button.UP in ev3.buttons.pressed() and curRound < 4 and not isRunning:
        curRound += 1
        sleep(0.3)

    #Downer button
    elif Button.DOWN in ev3.buttons.pressed() and curRound > 1 and not isRunning:
        curRound -= 1
        sleep(0.3)

    #Right button, which exits the program and resets the current round to the first
    elif Button.RIGHT in ev3.buttons.pressed() and not isRunning:  
        Text.write("1\n")
        Text.close()
        break

    #Left up (back) button, which exits and saves the last known "current round", and for next it starts with that saved round 
    elif Button.LEFT_UP in ev3.buttons.pressed() and not isRunning:
        Text.close()
        break
    
    #Refreshing the screen
    ev3.screen.clear()
    ev3.screen.draw_text(0, 40, "Current round: "+Rounds[curRound-1])
