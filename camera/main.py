from cameraSetttings import Camera

camera = Camera()
camera.start()
while camera.isRecording:
    camera.detectLineInFrame(preview=False, saveOutput=False)
    camera.wait(ms=1, exitKey='q')
camera.stop()