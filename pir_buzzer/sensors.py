import RPi.GPIO as GPIO
import time

pir_pin = 23
buzzer_pin = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)


def main():
    motion_detection()


def beep(repeat):
    for i in range(0, repeat):
        for pulse in range(60):
            GPIO.output(buzzer_pin, True)
            time.sleep(0.001)
            GPIO.output(buzzer_pin, False)
            time.sleep(0.001)
        time.sleep(0.02)


def motion_detection():
    while True:
        if GPIO.input(pir_pin):
            print("Motion detected")
            beep(4)
        time.sleep(0.2)


if __name__ == "__main__":
    main()
