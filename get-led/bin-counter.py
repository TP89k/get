import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
up_button = 20
down_button = 21

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
GPIO.setup(up_button, GPIO.IN)
GPIO.setup(down_button, GPIO.IN)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

while True:
    if GPIO.input(up_button):
        num = num + 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    
    if GPIO.input(down_button):
        num = num - 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    
    if num > 255:
        num = 0
    if num < 0:
        num = 255
    
    GPIO.output(leds, dec2bin(num))
    time.sleep(0.01)