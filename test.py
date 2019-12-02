import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(23, GPIO.IN)
GPIO.output(25, GPIO.LOW)
while True:
    if GPIO.input(23):
        GPIO.output(25, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(25, GPIO.LOW)
        

