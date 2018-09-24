from sense_hat import SenseHat
from time import sleep
from random import randint
import os
import sys

sense = SenseHat()
speed = 0

def pick_random_colour():
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)
    return(random_red, random_green, random_blue)

def easing(total):
    global speed
    while total <= 64:
        speed += 0.002
        return sleep(speed)
try:
    sense = SenseHat()
    sense.set_imu_config(False, False, True)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)

def main():
    sense.clear()
    i = 0
    while True:
        for y in range(0, 8):
            for x in range(0, 8):
                sense.set_pixel(x, y, pick_random_colour())
                easing((x+1)*(y+1))
                sense.clear()
            
    
        
if __name__ == "__main__":
    try:
        main()
    except(KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sys.exit(0)