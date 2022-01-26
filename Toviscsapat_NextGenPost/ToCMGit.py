from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Direction, Button
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the EV3 brick.
ev3 = EV3Brick()

# Configure 2 motors on Ports B and C.  Set the motor directions to
# counterclockwise, so that positive speed values make the robot move
# forward.  These will be the left and right motors of the Tank Bot.
left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)

# The wheel diameter of the Tank Bot is about 54 mm.
WHEEL_DIAMETER = 54

# The axle track is the distance between the centers of each of the
# wheels.  This is about 200 mm for the Tank Bot.
AXLE_TRACK = 200

# The Driving Base is comprised of 2 motors.  There is a wheel on each
# motor.  The wheel diameter and axle track values are used to make the
# motors move at the correct speed when you give a drive command.
robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)

robot.straight(40)