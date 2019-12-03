import RPi.GPIO as GPIO
import time
import requests

#GPIO SETUP
channel = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
URL = "http://localhost:5000/emergencyAlert"
data = {
        'vehicle_no': 'ch 01 j 7091',
        'latitude': 
        'longitude': 
}

def callback(channel):
        if GPIO.input(channel):
                print "Movement Detected!"
                requests.post()
        else:
                print "Movement Detected!"

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)