import time
import keyboard
from pynput.mouse import Button, Controller
import os

mouse = Controller()

os.system("clear")

print('Put your mouse in the spot you want to mine')
print('Saving spot #1 in 3 seconds...')
time.sleep(3)
pos_one = mouse.position
print('Saved #1')


print('Put your mouse in the spot you want to mine')
print(' ')
print('Saving spot #2 in 3 seconds...')
time.sleep(3)
pos_two = mouse.position
print('Saved #2')

print('Put your mouse in the spot you want to mine')
print(' ')
print('Saving spot #3 in 3 seconds...')
time.sleep(3)
pos_three = mouse.position
print('Saved #3')
time.sleep(1)

print('Put your mouse in the puffle tricks menu')
print(' ')
print('Saving in 3 seconds...')
time.sleep(3)
pos_puffle_tricks_menu = mouse.position
mouse.click(Button.left,1)
print('Saved puffle tricks menu')
time.sleep(1)
print(' ')

print('Put your mouse in the money bag icon from the puffle tricks menu')
print(' ')
print('Saving in 3 seconds...')
time.sleep(3)
pos_puffle_tricks_button = mouse.position
print('Saved money bag')

print(' ')

print('Starting...')

os.system('clear')

puffle_action_time = 0

def puffle_action():
    print('puffle mining action running')
    mouse.position = pos_puffle_tricks_menu
    time.sleep(1)
    mouse.click(Button.left,1)
    mouse.position = pos_puffle_tricks_button
    time.sleep(1)
    mouse.click(Button.left,1)

def run():
    global puffle_action_time
    global mouse

    if puffle_action_time == 4:
        puffle_action_time = 0
        puffle_action()
        os.system('clear')

    time.sleep(9)
    print('pos #1')
    mouse.position = pos_one
    #time.sleep(1)
    mouse.click(Button.left,1)
    time.sleep(2)
    keyboard.press_and_release('d')

    time.sleep(9)
    print('pos #2')
    mouse.position = pos_two
    #time.sleep(1)
    mouse.click(Button.left,1)
    time.sleep(2)
    keyboard.press_and_release('d')

    time.sleep(9)
    print('pos #3')
    mouse.position = pos_three
    #time.sleep(1)
    mouse.click(Button.left,1)
    time.sleep(2)
    keyboard.press_and_release('d')

    puffle_action_time += 1
    print('puffle action time is:', puffle_action_time)

while True:
    run()
    