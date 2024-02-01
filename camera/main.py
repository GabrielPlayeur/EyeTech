from cameraSettings import Camera

camera = Camera()
camera.start()
while camera.isRecording:
    camera.detectLineInFrame(preview=False, saveOutput=True)
    camera.wait(ms=1, exitKey='q')
camera.stop()