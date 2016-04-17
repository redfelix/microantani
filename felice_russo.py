from microbit import *
import random

while True:
	microbit.display.scroll("Benvenuti")
    	microbit.sleep(100)

	nomi = ["Pippo","Pluto","Paperino"]
	cose = ["Chitarra","Mandolino","pianoforte"]

	a = random.choice(nomi)
	b = random.choice(cose)

    	if button_a.is_pressed():
		display.scroll(a)
		microbit.sleep(100)
		display.scroll(b)
		microbit.sleep(300)
    	elif button_b.is_pressed():
    		display.scroll("ciaoo")
        	microbit.sleep(300)
