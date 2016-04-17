
import microbit
while True:                                     
    microbit.display.scroll("Hello python")
    microbit.sleep(100)

    if button_a.was_pressed():
        break
    elif button_b.was_pressed():
        display.show(Image.SAD)
 


