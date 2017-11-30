from picamera import PiCamera

camera = PiCamera()

for i in range (10):
    camera.capture("image.jpg")
