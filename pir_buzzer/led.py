import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

for x in range(0, 10):
    GPIO.output(8, True)
    time.sleep(0.5)
    GPIO.output(8, False)
    time.sleep(0.5)

GPIO.cleanup()
