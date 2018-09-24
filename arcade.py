from sense_hat import SenseHat
from time import sleep
import math
from random import randint
import os
import sys

blue = (255, 255, 0)

def random_character(size):
    sense.clear()
    for x in range(size//2):
        for y in range(size):
            if randint(0,1):
                sense.set_pixel(x, y, blue)
                sense.set_pixel(((size-1)-x), y, blue)
    sleep(1)        
        
try:
    sense = SenseHat()
    sense.set_imu_config(False, False, True)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)

def main():
    size = int(input('Kies een getal tussen 1 en 8: '))
    if (size > 8):
        print('Dit getal is hoger dan 8 :(')
    else:
        while True:
            random_character(size)
    
        
if __name__ == "__main__":
    try:
        main()
    except(KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sys.exit(0)