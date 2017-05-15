#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN)
GPIO.setup(8,GPIO.OUT)


while True:
    i=GPIO.input(10)
    if i==0:                 
        print "PIR not working ",i 
        GPIO.output(8, 0) 
        time.sleep(1)
    elif i==1:              
        print "PIR worked ",i
        GPIO.output(8, 1)
	pwm=GPIO.PWM(8,100)
	pwm.start(5)
 
	angle1=10
	duty1= float(angle1)/10 + 2.5              
 
	angle2=160
	duty2= float(angle2)/10 + 2.5
 
	ck=0
	while ck<=1:
     		pwm.ChangeDutyCycle(duty1)
     		time.sleep(1)
     		pwm.ChangeDutyCycle(duty2)
     		time.sleep(1)
     		ck=ck+1
             
	time.sleep(1)
GPIO.cleanup()	     
