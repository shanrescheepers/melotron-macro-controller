# Ja - kom en download maar my file.

import time
import digitalio
import board
import adafruit_matrixkeypad
import rotaryio
import usb_hid
import adafruit_rgbled
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

btn1 = digitalio.DigitalInOut(board.GP15)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(board.GP14)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

btn3 = digitalio.DigitalInOut(board.GP13)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.UP

btn4 = digitalio.DigitalInOut(board.GP12)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.UP

btn5 = digitalio.DigitalInOut(board.GP11)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.UP

btn6 = digitalio.DigitalInOut(board.GP10)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.UP

switch = digitalio.DigitalInOut(board.GP6)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

red = board.GP18
blue = board.GP19
green = board.GP20
led = adafruit_rgbled.RGBLED(red, blue, green)
led.color = (0, 0, 0)


cols = [digitalio.DigitalInOut(x) for x in (
    board.GP0, board.GP1, board.GP2, board.GP3)]
rows = [digitalio.DigitalInOut(x) for x in (
    board.GP4, board.GP5, board.GP9, board.GP7, board.GP8)]

keys = ((Keycode.L, Keycode.QUOTE, Keycode.SEMICOLON, Keycode.P), (Keycode.J, Keycode.U, Keycode.K, Keycode.O), (Keycode.T, Keycode.G, Keycode.H, Keycode.Y),
        (Keycode.D, Keycode.D, Keycode.Q, Keycode.F), (Keycode.S, Keycode.A, Keycode.W, Keycode.E))

kbd = Keyboard(usb_hid.devices)
kbd_layout = KeyboardLayoutUS(kbd)

encoder = rotaryio.IncrementalEncoder(board.GP17, board.GP16)
last_position = 0

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
print("start")
while True:
    keys = keypad.pressed_keys
    if keys:
        print("Pressed: ", keys)
        # kbd_layout.write(str(keys[0]).lower())
        for key in range(len(keys)):
            # kbd.press(keys[key])

            print(key)
            # time.sleep(0.09)
    else:
        kbd.release_all()

    if btn1.value is False:
        print("Btn1")

    if btn2.value is False:
        print("btn2")

    if btn3.value is False:
        print("btn3")

    if btn4.value is False:
        print("btn4")

    if btn5.value is False:
        print("btn5")

    if btn6.value is False:
        print("btn6")

    if switch.value is False:
        print("Switch")
        led.color = (240, 0, 240)
    else:
        led.color = (0, 0, 0)
    position = encoder.position
    if last_position is None or position != last_position:
        pos = position-last_position
        print(pos)
    last_position = position

  # Aan die einde, doen hierdie
    time.sleep(0.1)
