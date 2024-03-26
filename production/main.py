from controller import Controller

controller = Controller()
controller.onMotor.start()
controller.waiting()
while controller.isRunning:
    controller.start()
    controller.waiting()
controller.shutdown()