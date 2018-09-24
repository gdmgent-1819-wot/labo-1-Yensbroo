from sense_hat import SenseHat
from time import sleep
import os
import sys
sense = SenseHat()

s = (255, 204, 153)
w = (255, 255, 255)
r = (255, 0, 0)
b = (0, 0, 255)
br = (153, 76, 0)
bl = (0, 0, 0)
db = (51, 25, 0)



mario_pixels = [
    bl, bl, bl, r, r, r, w, bl,
    bl, bl, bl, r, r, r, r, r,
    bl, bl, s, s, s, bl, s, bl,
    bl, bl, s, s, s, s, s, s,
    bl, bl, bl, s, s, s, s, bl,
    bl, r, r, w, b, b, w, bl,
    w, bl, b, b, b, b, bl, w,
    bl, bl, br, bl, bl, bl, br, bl,
    ]

mario_pixels_jump = [
    bl, bl, bl, r, r, r, r, r,
    bl, bl, s, s, s, bl, s, bl,
    bl, bl, s, s, s, s, s, s,
    bl, bl, bl, s, s, s, s, bl,
    bl, r, r, w, b, b, w, bl,
    w, bl, b, b, b, b, bl, w,
    bl, bl, br, bl, bl, bl, br, bl,
    bl, bl, bl, bl, bl, bl, bl, bl
    ]

def mario_up():
    sense.set_pixels(mario_pixels_jump)
    sleep(0.1)
    sense.set_pixels(mario_pixels)

sense.set_pixels(mario_pixels)
sense.stick.direction_up = mario_up

try:
    sense = SenseHat()
    sense.set_imu_config(False, False, True)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)

def main():
    sense.set_pixels(mario_pixels)
    sense.stick.direction_up = mario_up
    
        
if __name__ == "__main__":
    try:
        main()
    except(KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sys.exit(0)


