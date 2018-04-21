import datetime as dt
import subprocess
import time
from threading import Thread

from RPi import GPIO

from lib import config


# TODO: Mudar o nome do arquivo

class LedIndicador(Thread):
    def __init__(self):
        super().__init__()
        self.alerta = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup((config.ALR['ledvm'], config.ALR['ledvr']), GPIO.OUT, initial=GPIO.LOW)

    def run(self):
        while True:
            if self.alerta is True:
                GPIO.output(config.ALR['ledvm'], GPIO.HIGH)
                time.sleep(1)
                GPIO.output(config.ALR['ledvm'], GPIO.LOW)
                time.sleep(2)

            else:
                GPIO.output(config.ALR['ledvr'], GPIO.HIGH)
                time.sleep(1)
                GPIO.output(config.ALR['ledvr'], GPIO.LOW)
                time.sleep(5)


class Camera(Thread):
    def __init__(self):
        super().__init__()

    @staticmethod
    def foto():
        agora = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

        # TODO: salvar em diretorio especifico
        # TODO: deixar em aberto ou singleshots?
        # TODO: fast shutter?
        subprocess.run(['raspistill', '-a', '12', '-md', '1', '-o' , agora + '.jpg', '-n', '-t', '1000'])

    # TODO: implementar isso aqui


'''
    def video(self):
        agora = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

        subprocess.run(['raspivid', '-a', '12', agora, '.h264', '-n'])
'''


def email():
    # config.ALR['email']
    pass


def telefone():
    # config.ALR['telefone']
    pass


def dash_alerta():
    pass
