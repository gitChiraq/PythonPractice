import keyboard
#When esc is pressed, the script will write something with a delay
#between each keypress
keyboard.wait('esc')
keyboard.send('A')
keyboard.write('HI', delay=5)
#keyboard.press_and_release('A')