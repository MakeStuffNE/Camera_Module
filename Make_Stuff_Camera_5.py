from picamera import PiCamera
from time import sleep
from gpiozero import Button


button = Button(3)
camera = PiCamera()

camera.rotation = 180

camera.start_preview()
button.wait_for_press()
camera.capture('/home/pi/Desktop/Snap.jpg')
camera.stop_preview()
