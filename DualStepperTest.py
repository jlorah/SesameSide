
#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperM$

import time
import atexit

#step 1: 

mh = Adafruit_MotorHAT(addr = 0x60)
Axis1 = mh.getStepper(200,1)
Axis2 = mh.getStepper(200,2)


#make a wrapper for threading
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

def stepper_worker(stepper, numsteps, direction, style)
   #print("onestep")
   stepper.step(numsteps, direction, style)
   #print("Done")



H = threading.Thread(target=stepper_worker, args=(axis1, numsteps, direction, step_style)
S = threading.Thread(target=stepper_worker, args=(axis2, numsteps, direction, step_style)

#creating an object
