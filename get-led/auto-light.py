import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
sensor = 6

GPIO.setup(led, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

while True:
    # Если датчик освещенности = 1 (светло), светодиод выключен (0)
    # Если датчик = 0 (темно), светодиод включен (1)
    light_state = GPIO.input(sensor)
    GPIO.output(led, not light_state)
    time.sleep(0.1)
