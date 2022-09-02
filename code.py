# Ja - kom en download maar my file.

from random import random
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
counter = 0
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
redVal = 0
greenVal = 0
blueVal = 0
newStandby = True
upDown = True

led = adafruit_rgbled.RGBLED(red, blue, green)
led.color = (redVal, greenVal, blueVal)


cols = [digitalio.DigitalInOut(x) for x in (
    board.GP0, board.GP1, board.GP2, board.GP3)]
rows = [digitalio.DigitalInOut(x) for x in (
    board.GP4, board.GP5, board.GP9, board.GP7, board.GP8)]

keys = ((Keycode.QUOTE, Keycode.L, Keycode.SEMICOLON, Keycode.P), (Keycode.O, Keycode.K, Keycode.U, Keycode.J), (Keycode.E, Keycode.S, Keycode.W, Keycode.A),
        (Keycode.D, Keycode.T, Keycode.F, Keycode.T), (Keycode.H, Keycode.T, Keycode.Y, Keycode.G))
# ffftgyol;ll'
kbd = Keyboard(usb_hid.devices)
kbd_layout = KeyboardLayoutUS(kbd)

encoder = rotaryio.IncrementalEncoder(board.GP17, board.GP16)
last_position = 0

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
print("start")
while True:
    # print(counter)
    counter += 1

    keys = keypad.pressed_keys
    # met die max keys, try = catch. dws, enige exceptions.
    try:
        if keys:
            print("Pressed: ", keys)

        # kbd_layout.write(str(keys[0]).lower())
            for key in range(len(keys)):
                counter = 0

                kbd.press(keys[key])

                print(key)
                # time.sleep(0.09)
        else:
            kbd.release_all()
    except:
        print("Max Keys")

    if btn1.value is False:
        print("Btn1")
        kbd.press(Keycode.COMMAND, Keycode.K)
        time.sleep(.3)
    if btn2.value is False:
        print("btn2")
        kbd.send(Keycode.TAB)
        time.sleep(.3)
    else:
        kbd.release(Keycode.TAB)
    if btn3.value is False:
        print("btn3")
        kbd.press(Keycode.ENTER)
        time.sleep(.3)
    if btn4.value is False:
        print("btn4")
        kbd.press(Keycode.SPACEBAR)
        time.sleep(.3)
    if btn5.value is False:
        print("btn5")
        kbd.press(Keycode.R)
        time.sleep(.3)
    if btn6.value is False:
        print("btn6")
        kbd.press(Keycode.B)
        time.sleep(.3)

    if switch.value is False:
        #     print("Switch")
        if counter > 300:
            if newStandby:
                newStandby = False
                redVal = 0
                greenVal = 0
                blueVal = 0
            print("Standby")
            if upDown:
                redVal += 1
                if redVal == 256:
                    redVal = 255
                    greenVal += 1
                if greenVal == 256:
                    greenVal = 255
                    blueVal += 1
                if blueVal == 256:
                    blueVal = 255
                    upDown = False
            else:
                redVal -= 1
                if redVal == -1:
                    redVal = 0
                    greenVal -= 1
                if greenVal == -1:
                    greenVal = 0
                    blueVal -= 1
                if blueVal == -1:
                    blueVal = 0
                    upDown = True

        else:
            redVal = 240
            greenVal = 0
            blueVal = 240
    else:
        newStandby = True
        counter = 0
        redVal = 0
        greenVal = 0
        blueVal = 0

    position = encoder.position

    if last_position is None or position != last_position:
        pos = position-last_position
        print(pos)
        if pos > -1:
            kbd.press(Keycode.X)
        if pos < 1:
            kbd.press(Keycode.Z)
        last_position = position

    # print("Red", redVal)
    # print("Green", greenVal)
    # print("Blue", blueVal)
    led.color = (redVal, greenVal, blueVal)
  # Aan die einde, doen hierdie
