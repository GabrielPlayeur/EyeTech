from controller import Controller
from time import time
controller = Controller()
while True:
    controller.waiting()
    controller.start()
    controller.shutdown()