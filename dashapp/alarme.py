from dashapp import config, inicio
from RPi import GPIO
from threading import Thread
import time


class LEDIndicador(Thread):
    def __init__(self):
        super().__init__()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup((config.ALR['ledvm'], config.ALR['ledvr']), GPIO.OUT, initial=GPIO.LOW)

    def run(self):
        while True:
            if inicio.alerta is True:
                GPIO.output(config.ALR['ledvm'], GPIO.HIGH)
                time.sleep(1)
                GPIO.output(config.ALR['ledvm'], GPIO.LOW)
                time.sleep(2)

            else:
                GPIO.output(config.ALR['ledvr'], GPIO.HIGH)
                time.sleep(1)
                GPIO.output(config.ALR['ledvr'], GPIO.LOW)
                time.sleep(5)


def email():
    # config.ALR['email']
    pass


def telefone():
    # config.ALR['telefone']
    pass


def dashAlerta():
    pass
