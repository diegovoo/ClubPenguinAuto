import time
import keyboard
from pynput.mouse import Button, Controller
import os

mouse = Controller()

os.system("clear")

print('Put your mouse in the buy button')
print('Saving spot in 3 seconds...')
time.sleep(3)
pos_buy_button = mouse.position
print('Saved spot')

print('Put your mouse over the yes button')
print('Saving spot in 3 seconds...')
time.sleep(3)
pos_yes_button = mouse.position
print('Saved spot')

os.system('clear')

times_bought = 0

def run():
    global mouse
    global times_bought
    
    print('times bought: ' + str(times_bought))

    mouse.position = pos_buy_button
    mouse.click(Button.left,1)
    time.sleep(0.5)
    
    mouse.position = pos_yes_button
    mouse.click(Button.left,1)
    time.sleep(0.5)

    mouse.position = pos_yes_button # clicks the 'Ok' button
    mouse.click(Button.left,1)
    time.sleep(0.5)

    times_bought += 1

while True:
    run()