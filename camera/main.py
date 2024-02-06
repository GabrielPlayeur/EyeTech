from cameraSettings import Camera

camera = Camera()
camera.start()
while camera.isRecording:
    camera.detectLineInFrame(preview=False, saveOutput=False)
camera.stop()