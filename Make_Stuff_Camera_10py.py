from picamera import PiCamera
from os import system

camera = PiCamera()
camera.resolution = (1024,768)

for i in range (10):
    camera.capture("image{0:04d}.jpg".format(i))

system("convert -delay 10 -loop 0 image*.jpg animation.gif")
print("Animation created Makers!!!")
