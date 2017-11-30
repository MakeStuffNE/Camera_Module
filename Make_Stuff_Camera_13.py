from guizero import App
from gpiozero import Button
from picamera import PiCamera
from time import sleep, gmtime, strftime
from overlay_functions import *

next_overlay_btn = Button(13)
take_pic_btn = Button (21)

def next_overlay():
    global overlay
    overlay = next(all_overlays)
    preview_overlay(camera, overlay)

def take_picture():
    camera.capture(output)
    camera.stop_preview()
    remove_overlays(camera)
    output_overlay(output, overlay)

next_overlay_btn.when_pressed = next_overlay
take_pic_btn.when_pressed = take_picture

camera = PiCamera()
camera.resolution = (800,480)
camera.hflip = True
camera.start_preview(alpha = 128)

output = strftime("/home/pi/Make_Stuff_Modules/Camera_Module/Selfie_Booth/image-%d-%m %H:%M.png", gmtime())

