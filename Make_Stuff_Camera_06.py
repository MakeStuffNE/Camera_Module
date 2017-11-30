from picamera import PiCamera
from time import sleep
from gpiozero import Button


button = Button(3)
camera = PiCamera()
frame = 1

camera.rotation = 180

camera.start_preview()

while True:
    try:
        button.wait_for_press()
        camera.capture('/home/pi/Make_Stuff_Modules/Camera_Module/Our_StopFrame/frame%03d.jpg' % frame)
        frame = frame + 1
        
    except KeyboardInterrupt:
        camera.stop_preview()
        break
        
