import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
print 'ROBBER ATTACKS'
GPIO.output(23,GPIO.HIGH)
GPIO.output(18,GPIO.HIGH)
time.sleep(2)

GPIO.output(23,GPIO.LOW)
GPIO.output(18,GPIO.LOW)