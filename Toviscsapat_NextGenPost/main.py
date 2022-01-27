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

# Write your program here.
ev3 = EV3Brick()
gyro = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)
gyro.reset_angle(0)
color1 = ColorSensor(Port.S2)
color2 = ColorSensor(Port.S3)
AMotor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
BMotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
CMotor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
DMotor = Motor(Port.D, positive_direction=Direction.CLOCKWISE)


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

#Containers round
MedMotor(-200, 120, "D", [8, 18])
AbsDRV(30, 100, 25, gyro)
LFOL(color1, color2, 70, 100, 1, 4)
# AbsDRV(100, 100, 70, gyro)
# wait(1000000)
LFOL(color1, color2, 70, 40, 0.7, 3)
wait(1500)
print(gyro.angle())
#This goes to the rails:
# AbsTU(225, 100, gyro)
# print(gyro.angle())
# wait(1500)
# AbsDRV(225, -100, -20, gyro)
# # print(gyro.angle())
# AbsTU(180, 100, gyro)
# LFOL(color1, color2, 70, 30, 2, 2)
# wait(1000)
# MedMotor(100, 35, "A", [1, 2])
# wait(1500)
# MedMotor(-100, 35, "A", [1, 2])
# AbsDRV(180, -100, -15, gyro)
# wait(1000)
# AbsTU(270, 100, gyro)
# wait(1000)
# AbsDRV(270, 100, 15, gyro)
# wait(1000)
AbsTU(183, 100, gyro)
MedMotor(100, 50, "A", [1, 2])
AbsDRV(183, 200, 48, gyro)
wait(2000)
MedMotor(-100, 42, "A", [1, 2])
AbsDRV(180, -100, -35, gyro)
AbsTU(90, 100, gyro)
AbsDRV(75, -100, -255, gyro)

#Airplane round
# print(gyro.angle())
# AbsDRV(0, 100, 20, gyro)
# print(gyro.angle())
# LFOL(color1, color2, 100, 50, 1.3, 3)
# print(gyro.angle())
# Align(color1, color2)
# print(gyro.angle())
# MedMotor(130, 200, "D", [1, 1.2])
# wait(1000)
# MedMotor(-130, 200, "D", [1, 1.2])
# MedMotor(130, 200, "A", [1, 1.2])
# print(gyro.angle())
# AbsDRV(60, 100, 13, gyro)
# MedMotor(-130, 100, "A", [1, 1.2])
# MedMotor(130, 80, "A", [1, 1.2])
# print(gyro.angle())
# AbsDRV(45, -150, -20, gyro)
# AbsDRV(45, -200, -50, gyro)

# Western round
# wait(1000)
# MedMotor(200, 90, "A", [12, 22])
# Drive(200, 64, 0)
# wait(1000)
# NoGyroTU(-200, 55)
# wait(1000)
# MedMotor(200, 150, "D", [12, 20])
# wait(1000)
# MedMotor(-200, 80, "D", [12, 20])
# wait(1000)
# NoGyroTU(200, 130)
# wait(1000)
# MedMotor(200, 80, "D", [12, 20])
# wait(1000)
# Drive(200, 15, 0)
# wait(1000)
# MedMotor(-200, 60, "D", [12, 20])

# Second round
# AbsDRV(0, 50, 15, gyro)
# wait(1000)
# #LFOL 177cm
# LFOL(color1, color2, 80, 80, 1.3, 5)
# wait(500)
# MedMotor(100, 167, "A", [1.67, 1])
# wait(500)
# LFOL(color1, color2, 80, 60, 1.3, 5)
# wait(500)
# MedMotor(100, 105, "A", [1.67, 1])
# wait(500)
# LFOL(color1, color2, 80, 50, 1.3, 5)
# wait(500)
# MedMotor(100, 180, "D", [1, 1])
# wait(500)
# LFOL(color1, color2, 80, 20, 1.3, 5)

# NoGyroTU(200, 230)
# wait(1000)
# AbsTU(90, 100, gyro)
# wait(1000)
# AbsDRV(90, 200, 30, gyro)

# Master Menu
# Somehow it looks like the is_alive() part of threading doesn't work with EV3 Micropython, so I try a more single minded method, using a boolean variable, isRunning
isRunning = False


def Running(Runs):
    global isRunning
    isRunning = Runs


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
        # LFOL 177cm
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
        print("Third round")
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
    Running(False)


# from rounds import Round
curRound = 1
Rounds = ["Containers", "Tower", "Airplane", "Last"]
screen = Image("Screen", sub=False)
font = Font(family=None, size=14)
ev3.screen.set_font(font)
# p = Process(target=Round, args=(curRound))
# p.start()
# p.join()
# t1 = threading.Thread(target=Round, args=(curRound))
# t1.start()
# if __name__=="__main__":
# savedData = DataLog("1", name="CurrentRound", timestamp=False, extension="txt")
text = open("CurrentRound.txt", "r")
txt = text.readlines()
print(txt)
print(len(txt))
curRound = int(txt[len(txt)-1].replace("\n", ""))
text.close()
Text = open("CurrentRound.txt", "w")
while True:
    Text.write(str(curRound)+"\n")
    # textFile = open("CurrentRound.txt", "w")
    # savedData.log(curRound)
    # print(savedData)
    sleep(0.3)
    # textFile.close()
    # print(int(textFile.read()))
    # print(t1.is_alive())
    # print(isRunning)
    # print(curRound)
    if Button.CENTER in ev3.buttons.pressed() and not isRunning:
        gyro.reset_angle(0)
        # color1.reset()
        # color2.reset()
        AMotor.reset_angle(0)
        BMotor.reset_angle(0)
        CMotor.reset_angle(0)
        DMotor.reset_angle(0)
        ev3.speaker.play_file(SoundFile.READY)
        # isRunning = True
        # Round(curRound), stop()
        # isRunning = False
        # p = Process(target=Round, args=(curRound))
        # p.start()
        Round(curRound)
        # p.join()
        # if __name__=="__main__":
        sleep(0.5)
        if curRound < 4:
            curRound += 1
            # print("Stop")
            # Stop()
            # isRunning = False
    elif Button.UP in ev3.buttons.pressed() and curRound < 4 and not isRunning:
        curRound += 1
        sleep(0.3)
    elif Button.DOWN in ev3.buttons.pressed() and curRound > 1 and not isRunning:
        curRound -= 1
        sleep(0.3)
    elif Button.RIGHT in ev3.buttons.pressed() and not isRunning: #curRound == 1 and 
        # if __name__=="__main__":
        # savedData.log("1")
        Text.write("1\n")
        Text.close()
        break
        sleep(0.5)
        # p.join()
        # isRunning = True
        # Round(5), stop()
        # isRunning = False
        curRound += 1
    elif Button.LEFT_UP in ev3.buttons.pressed() and not isRunning: #curRound == 1 and 
        # if __name__=="__main__":
        # p.join()
        Text.close()
        print("bal gomb")
        break
        # isRunning = True
        # Round(6), stop()
        # isRunning = False
        curRound += 1
    ev3.screen.clear()
    # note: font size is too big; ignore mulitprocessing and save current round in a text file instead; do restart function with file-reading method
    ev3.screen.draw_text(0, 40, "Current round: "+Rounds[curRound-1])