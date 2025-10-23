from flask import Flask, render_template
import json
import threading
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

alive = 0
data = {}

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
    data["alarm"] = False
    while True:
        if GPIO.input(pir_pin):
            print("Motion detected")
            beep(4)
            data["motion"] = 1
        else:
            data["motion"] = 0
        if data["alarm"]:
            beep(2)
        time.sleep(1)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/keep_alive")
def keep_alive()->str:
    global alive, data
    alive += 1
    keep_alive_count = str(alive)
    data["keep_alive"] = keep_alive_count
    parsed_json = json.dumps(data)
    return str(parsed_json)


@app.route("/status=<name>-<action>", methods=["POST"])
def status(name:str, action:str)->str:
    global data
    if name == "buzzer":
        if action == "on":
            data["alarm"] = True
        elif action == "off":
            data["alarm"] = False
    return str("ok")


if __name__ == '__main__':
    sensors_thread = threading.Thread(target=motion_detection)
    sensors_thread.start()
    app.run(host="172.20.10.3", port=80)
