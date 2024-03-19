from controller import Controller

controller = Controller()
#TODO : vibration debut
controller.waiting()
while controller.isRunning:
    controller.start()
    controller.waiting()
controller.shutdown()