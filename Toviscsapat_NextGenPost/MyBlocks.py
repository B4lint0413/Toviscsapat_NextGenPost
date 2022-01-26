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
    for i in transmission:
        if transmission.index(i) != 0:
            szum = szum / i
        else:
            szum = i
    # if len(transmission)%2 == 0{
    #     speed = Speed*-1
    # }else{
    #     speed = Speed
    # }
    TargRot = angle/szum
    # motor.reset_angle(0)
    if speed > 0:
        while abs(motor.angle()) < TargRot:
            motor.run(speed)
    else:
        while -motor.angle() < TargRot:
            motor.run(speed)
    motor.stop()

def NoGyroTU (speed, angle):
    # 12 cm a kerekek közti táv
    distance = 12
    ev3 = EV3Brick()
    diameter = 14.34
    TargRotation =  (distance*3.14/360*angle)/(diameter*3.14)
    BMotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
    CMotor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)

    # BMotor.reset_angle(0)
    # CMotor.reset_angle(0)
    while (abs(BMotor.angle())/360 <= TargRotation):
        BMotor.run(speed)
        CMotor.run(-speed)
    BMotor.stop()
    CMotor.stop()    

def AbsTU(toAngle, speed, gyro):
    #
    ev3 = EV3Brick()
    BMotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
    CMotor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
    startAng = (360+(gyro.angle()%360))%360
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
    #To negate the AbsDRV negate the speed and the cm too
    ev3 = EV3Brick()
    BMotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
    CMotor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
    Speed = speed
    DRV = DriveBase(BMotor, CMotor, 81.6, 105)
    CM = cm
    TargetRot = ((BMotor.angle()+CMotor.angle())/2)+CM/(8.16*3.1416)*360
    #startAng = (360+(gyro.angle()%360))%360
    #gyro.reset_angle(startAng)

    # BMotor.reset_angle(0)
    # CMotor.reset_angle(0)
    if CM > 0:
        while ((BMotor.angle() + CMotor.angle())/2 < TargetRot):
            DRV.drive(Speed, toAngle-(gyro.angle()%360))
    else:
        while ((BMotor.angle() + CMotor.angle())/2 > TargetRot):
            DRV.drive(Speed, toAngle-(gyro.angle()%360))
    DRV.stop()
def Align(sensor1, sensor2, speed):
    #Feature idea: calibrate the definition of black(reflected) before running
    # sensor1 is the sensor on the left side; sensor2 is the sensor on the right side
    ev3 = EV3Brick()
    BMotor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
    CMotor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
    DRV = DriveBase(BMotor, CMotor, 81.6, 105)
    #startAng = (360+(gyro.angle()%360))%360
    #gyro.reset_angle(startAng)

    # BMotor.reset_angle(0)
    # CMotor.reset_angle(0)
    while sensor1.reflection()>=20 or sensor2.reflection()>=20:
        if sensor1.reflection()>=20:
            BMotor.run(sensor1.reflection()*1)#speed
        else:
            BMotor.hold()
        if sensor2.reflection()>=20:
            CMotor.run(sensor2.reflection()*1)#speed
        else:
            CMotor.hold()

def LFOL(sensor1, sensor2, speed, cm, k, mode):
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
    #startAng = (360+(gyro.angle()%360))%360
    #gyro.reset_angle(startAng)

    # BMotor.reset_angle(0)
    # CMotor.reset_angle(0)
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
