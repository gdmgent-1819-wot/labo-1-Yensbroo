from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

def pick_random_colour():
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)
    return(random_red, random_green, random_blue)

def easing(total, speed):
    while total < 64:
        print(total)
        speed += 0.1
        if total == 64:
            speed = 0
        return(speed)
        

    
sense.clear()
i = 0
while True:
    for y in range(0, 8):
        for x in range(0, 8):
            sense.set_pixel(x, y, pick_random_colour())
            sleep(0.1)
            sense.clear()
            