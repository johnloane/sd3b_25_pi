from gpiozero import MotionSensor, TonalBuzzer
import time


pir = MotionSensor(23)
buzzer = TonalBuzzer(24)

pir.wait_for_no_motion()

while True:
    print("Ready")
    pir.wait_for_no_motion()
    print("Motion detected")
    buzzer.play("A4")
    time.sleep(0.1)
    buzzer.stop()
