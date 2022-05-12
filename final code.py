# Write your code here :-)
# SPDX-FileCopyrightText: 2017 John Edgar Park for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# FruitBox Sequencer
# for Adafruit Circuit Playground express
# with CircuitPython

import time

from adafruit_circuitplayground.express import cpx

# Change this number to adjust touch sensitivity threshold, 0 is default
cpx.adjust_touch_threshold(600)

bpm = 140  # quarter note beats per minute, change this to suit your tempo

beat = 15 / bpm  # 16th note expressed as seconds

WHITE = (30, 30, 30)
RED = (90, 0, 0)
YELLOW = (45, 45, 0)
GREEN = (0, 90, 0)
AQUA = (0, 45, 45)
BLUE = (0, 0, 90)
PURPLE = (45, 0, 45)
BLACK = (0, 0, 0)

cpx.pixels.brightness = 0.1  # set brightness value

# The seven files assigned to the touchpads
audio_files = ["kick.wav", "chop_snare.wav", "trap_hat.wav", "open_hat.wav"]

step_advance = 0  # to count steps
step = 0

# sixteen steps in a sequence
step_note = [2, 2, 2, 2, 1, 0, 2, 2, 2, 2, 2, 0, 1, 0, 2, 2]

# step pixels
step_pixel = [9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

# step colors
step_col = [WHITE, RED, YELLOW, GREEN, AQUA, BLUE, PURPLE, BLACK]


def prog_mode(index):
    cpx.play_file(audio_files[index])
    step_note[step] = index
    cpx.pixels[step_pixel[step]] = step_col[step_note[step]]
    print("playing file " + audio_files[index])

keyboardmode = True
apressed = 0

while True:
    if cpx.button_a AND cpx.button_b:
        print (apressed)
        apressed = apressed+1
        if apressed > 8:
            keyboardmode = not keyboardmode
            apressed = 0
            if cp.switch:
                print("Slide switch off!")
                cp.pixels.fill((0, 0, 0))
                cp.stop_tone()
                continue
            if cp.touch_A4:
                print('Touched A4!')
                cp.pixels.fill((15, 0, 0))
                cp.start_tone(262)
            elif cp.touch_A5:
                print('Touched A5!')
                cp.pixels.fill((15, 5, 0))
                cp.start_tone(294)
            elif cp.touch_A6:
                print('Touched A6!')
                cp.pixels.fill((15, 15, 0))
                cp.start_tone(330)
            elif cp.touch_A7:
                print('Touched A7!')
                cp.pixels.fill((0, 15, 0))
                cp.start_tone(349)
            elif cp.touch_A1:
                print('Touched A1!')
                cp.pixels.fill((0, 15, 15))
                cp.start_tone(392)
            elif cp.touch_A2 and not cp.touch_A3:
                print('Touched A2!')
                cp.pixels.fill((0, 0, 15))
                cp.start_tone(440)
            elif cp.touch_A3 and not cp.touch_A2:
                print('Touched A3!')
                cp.pixels.fill((5, 0, 15))
                cp.start_tone(494)
            elif cp.touch_A2 and cp.touch_A3:
                print('Touched "8"!')
                cp.pixels.fill((15, 0, 15))
                cp.start_tone(523)
            else:
                cp.pixels.fill((0, 0, 0))
                cp.stop_tone()





        print ("keyboard mode", keyboardmode)

        # playback mode
    if cpx.switch:  # switch is slid to the left, play mode

        cpx.red_led = False

        if cpx.button_a:
            cpx.pixels.fill(GREEN)
            time.sleep(.2)
            cpx.pixels.fill(BLACK)

        if cpx.button_b:
            for i in range(16):
                step = i
                # light a pixel
                cpx.pixels[step_pixel[i]] = step_col[step_note[i]]
                cpx.pixels[step_pixel[i - 1]] = BLACK

                # play a file
                cpx.play_file(audio_files[step_note[i]])

                # sleep a beat
                time.sleep(beat)
            cpx.pixels.fill(BLACK)

        if cp.touch_A4 and not cp.touch_A5:
                print('Touched A4!')
                cp.pixels.fill((15, 0, 0))
                cp.start_tone(262)
            elif cp.touch_A5 and not cp.touch_A4:
                print('Touched A5!')
                cp.pixels.fill((15, 5, 0))
                cp.start_tone(294)
            elif cp.touch_A6:
                print('Touched A6!')
                cp.pixels.fill((15, 15, 0))
                cp.start_tone(330)
            elif cp.touch_A7:
                print('Touched A7!')
                cp.pixels.fill((0, 15, 0))
                cp.start_tone(349)
            elif cp.touch_A1:
                print('Touched A1!')
                cp.pixels.fill((0, 15, 15))
                cp.start_tone(392)
            elif cp.touch_A2 and not cp.touch_A3:
                print('Touched A2!')
                cp.pixels.fill((0, 0, 15))
                cp.start_tone(440)
            elif cp.touch_A3 and not cp.touch_A2:
                print('Touched A3!')
                cp.pixels.fill((5, 0, 15))
                cp.start_tone(494)
            elif cp.touch_A2 and cp.touch_A3:
                print('Touched "8"!')
                cp.pixels.fill((15, 0, 15))
                cp.start_tone(523)
            elif: cp.touch_A4 and cp.touch_A5:
                print('playback mode')
                for i in range(16):
                    step = i
                # light a pixel
                    cpx.pixels[step_pixel[i]] = step_col[step_note[i]]
                    cpx.pixels[step_pixel[i - 1]] = BLACK

                # play a file
                    cpx.play_file(audio_files[step_note[i]])

                # sleep a beat
                    time.sleep(beat)
                cpx.pixels.fill(BLACK)

            else:
                cp.pixels.fill((0, 0, 0))
                cp.stop_tone()



    # beat programming mode
    else:  # switch is slid to the right, record mode
        cpx.red_led = True
        if cpx.button_a:  # clear pixels, reset step to first step
            cpx.pixels.fill(RED)
            time.sleep(.2)
            cpx.pixels.fill(BLACK)
            cpx.pixels[9] = WHITE
            step = 0
            step_advance = 0

        # press B button to advance neo pixel steps
        if cpx.button_b:  # button has been pressed
            step_advance += 1
            step = step_advance % 16
            cpx.play_file(audio_files[step_note[step]])
            cpx.pixels[step_pixel[step]] = step_col[step_note[step]]
            cpx.pixels[step_pixel[step - 1]] = BLACK

        if cpx.touch_A1:
            prog_mode(0)
        if cpx.touch_A2:
            prog_mode(1)
        if cpx.touch_A3:
            prog_mode(2)
        if cpx.touch_A4:
            prog_mode(3)



# Write your code here :-)
