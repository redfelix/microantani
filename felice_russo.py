from microbit import *
while True:                                     
    microbit.display.scroll("Hello python")
    microbit.sleep(100)

    if button_a.is_pressed():
        break
    elif button_b.is_pressed():
        display.show(Image.SAD)
 


