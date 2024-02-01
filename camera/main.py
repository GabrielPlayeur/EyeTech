from cameraSetttings import Camera
from timing import perf

camera = Camera()
camera.start()
while camera.isRecording:
    camera.detectLineInFrame(preview=False, saveOutput=True)
    camera.wait(ms=1, exitKey='q')
camera.stop()
print(perf)