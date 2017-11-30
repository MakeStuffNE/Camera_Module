from gpiozero import Button

next_overlay_btn = Button(13)
take_pic_btn = Button (21)

def next_overlay():
    print("Next Overlay")

def take_picture():
    print("Take a picture")

next_overlay_btn.when_pressed = next_overlay
take_pic_btn.when_pressed = take_picture

