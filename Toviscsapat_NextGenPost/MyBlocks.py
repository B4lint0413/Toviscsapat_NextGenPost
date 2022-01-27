#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


def Drive(speed, cm, steering):
    ev3 = EV3Brick()
    BMotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
    CMotor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
    Speed = speed
    DRV = DriveBase(BMotor, CMotor, 81.6, 105)
    CM = cm
    Steering = steering
    TargetRot = CM/(8.16*3.1416)*360

    BMotor.reset_angle(0)
    CMotor.reset_angle(0)
    while ((BMotor.angle() + CMotor.angle())/2 < TargetRot):
        DRV.drive(Speed, Steering)
    DRV.stop()

def MedMotor(speed, angle, port, transmission):
    #For negative rotation negate the speed
    #For port give the name of the wanted motor

    ev3 = EV3Brick()
    szum = 0 
    if port == "D":
        motor = Motor(Port.D, positive_direction=Direction.CLOCKWISE)
    elif port == "A":
        motor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
    
    #Counting transmission
    for i in transmission:
        if transmission.index(i) != 0:
            szum = szum / i
        else:
            szum = i
    TargRot = angle/szum

    #Moving the motor
    if speed > 0:
        while abs(motor.angle()) < TargRot:
            motor.run(speed)
    else:
        while -motor.angle() < TargRot:
            motor.run(speed)
    motor.stop()

def NoGyroTU (speed, angle):
    # 12 cm a kerekek közti táv
    #Turns the robot without the usage of gyro sensor
    distance = 12
    ev3 = EV3Brick()
    diameter = 14.34
    TargRotation =  (distance*3.14/360*angle)/(diameter*3.14)
    BMotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
    CMotor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)

    while (abs(BMotor.angle())/360 <= TargRotation):
        BMotor.run(speed)
        CMotor.run(-speed)
    BMotor.stop()
    CMotor.stop()    

def AbsTU(toAngle, speed, gyro):
    #Absolute turning which means that the given angle is not relative, it is always the same direction
    #North is 0, east is 90, south is 180 and west is 270
    ev3 = EV3Brick()
    BMotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
    CMotor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
    startAng = (360+(gyro.angle()%360))%360
    
    #Chosing the shorter way to turn (turning right or left)
    if(toAngle-startAng > 180):
        while (((360+(gyro.angle()%360))%360) != toAngle):
            BMotor.run((startAng-toAngle)/abs(toAngle-startAng)*speed)
            CMotor.run((startAng-toAngle)/abs(toAngle-startAng)*-speed)
    else:
        while (((360+(gyro.angle()%360))%360) != toAngle):
            BMotor.run((startAng-toAngle)/abs(toAngle-startAng)*-speed)
            CMotor.run((startAng-toAngle)/abs(toAngle-startAng)*speed)
    BMotor.stop()
    CMotor.stop()

def AbsDRV(toAngle, speed, cm, gyro):
    #It is the same as AbsTU, but it moves the robot forward (or backwards).
    #It was made to correct the AbsTU if gyro sensor wasn't precise. It inspects whether the robot is still in the wanted direction.
    #To negate the AbsDRV negate the speed and the cm too
    ev3 = EV3Brick()
    BMotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
    CMotor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
    Speed = speed
    DRV = DriveBase(BMotor, CMotor, 81.6, 105)
    CM = cm
    TargetRot = ((BMotor.angle()+CMotor.angle())/2)+CM/(8.16*3.1416)*360

    if CM > 0:
        while ((BMotor.angle() + CMotor.angle())/2 < TargetRot):
            DRV.drive(Speed, toAngle-(gyro.angle()%360))
    else:
        while ((BMotor.angle() + CMotor.angle())/2 > TargetRot):
            DRV.drive(Speed, toAngle-(gyro.angle()%360))
    DRV.stop()

def Align(sensor1, sensor2):
    #Feature idea: calibrate the definition of black(reflected) before running
    #It aligns the robot to a black line to make robot run more precise.
    # sensor1 is the sensor on the left side; sensor2 is the sensor on the right side
    ev3 = EV3Brick()
    BMotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
    CMotor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
    DRV = DriveBase(BMotor, CMotor, 81.6, 105)

    #It is slowing down as it approaches the black line.
    while sensor1.reflection()>=10 or sensor2.reflection()>=10:
        if sensor1.reflection()>=10:
            BMotor.run(sensor1.reflection()*1)#speed
        else:
            BMotor.hold()
        if sensor2.reflection()>=10:
            CMotor.run(sensor2.reflection()*1)#speed
        else:
            CMotor.hold()
    BMotor.stop()
    CMotor.stop()

def LFOL(sensor1, sensor2, speed, cm, k, mode):
    #PD (from PID controller) line following, to make smooth and precise line following.
    #We don't use the "I" factor, because it would be useful for longer line followings, for example at least 2 meters.
    #"P" is responsible for the error, the differrence between what we see with the sensor, and what we want to see.
    #We use "D" to take  last error in account to "predict" what will happen.
    # K is responsible for the amount of correction
    # sensor1 is the sensor on the left side; sensor2 is the sensor on the right side
    # Modes: mode 1: both sensors; mode 2: left sensor from right
    # mode 3: right sensor from right; mode 4: left sensor from left; mode 5: right sensor from left
    ev3 = EV3Brick()
    BMotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
    CMotor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
    DRV = DriveBase(BMotor, CMotor, 81.6, 105)
    CM = cm
    TargetRot = ((BMotor.angle()+CMotor.angle())/2)+CM/(8.16*3.1416)*360
    steering = 0
    lastError = 0

    if mode == 1:
        while ((BMotor.angle() + CMotor.angle())/2 < TargetRot):
            error = (40-sensor2.reflection())+(sensor1.reflection()-40)
            steering = error*k+(error-lastError)*k
            DRV.drive(speed, steering)
            lastError = error
        DRV.stop()
    elif mode == 2 or mode == 3:
        if mode == 3:
            sensor1 = sensor2
        while ((BMotor.angle() + CMotor.angle())/2 < TargetRot):
            error = ((sensor1.reflection()-10)-45)
            steering = error*k+(error-lastError)*k
            DRV.drive(speed, steering)
            lastError = error
        DRV.stop()
    elif mode == 4 or mode == 5:
        if mode == 4:
            sensor1 = sensor2
        while ((BMotor.angle() + CMotor.angle())/2 < TargetRot):
            error = ((sensor1.reflection()-10)-45)
            steering = error*k+(error-lastError)*k
            DRV.drive(speed, steering)
            lastError = error
        DRV.stop()
