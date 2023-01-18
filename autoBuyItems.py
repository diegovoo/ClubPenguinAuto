import time
import keyboard
from pynput.mouse import Button, Controller
import os

mouse = Controller()

os.system('clear')

print('Hover your mouse over the "yes" button')
print('Saving spot in 3 seconds...')
time.sleep(3)
pos_yes_button = mouse.position
print('Saved')

print('Hover your mouse over the "ok" button')
print('Saving spot in 3 seconds...')
time.sleep(3)
pos_ok_button = mouse.position
print('Saved')

os.system('clear')

def run():
    global mouse

    # Clicks on the item and opens buy menu
    mouse.click(Button.left,1)
    time.sleep(0.5)
    print('clicked')

    # Buys item
    mouse.position = pos_yes_button
    mouse.click(Button.left,1)
    #time.sleep(0.5)
    print('pos yes')

    mouse.position = pos_ok_button
    mouse.click(Button.left,1)
    print('pos ok')

while True:
    keyboard.wait('f')
    run()