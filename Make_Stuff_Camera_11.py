from picamera import PiCamera
from time import sleep

camera = PiCamera()

image_number = 0

while True:
    sleep(3600)
    image_name = "image{0:04}.jpg".format(image_number)
    camera.capture(image_name)
    image_number = image_number + 1
