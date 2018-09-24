from sense_hat import SenseHat
from time import sleep
from random import randint
import os
import sys

# set variables
black = (0, 0, 0)
white = (255, 255, 255)
thrown_numbers = []
player_1 = True
player_1_score = 0
player_2 = False
player_2_score = 0

# function to add score to variables
def add_score(score):
    global thrown_numbers
    global player_1
    global player_2
    global player_1_score
    global player_2_score
    # if the length of the array is equal or smaller than 4, add last thrown number to array
    if (len(thrown_numbers)) <= 4:
        thrown_numbers.append(score)
    # else go to next statements
    else:
        # if player_1 variable is true make total sum of numbers in array
        # empty the array
        # show message for player 2
        # set player_2 to True and player_1 to false
        if player_1:
            player_1_score = sum(thrown_numbers)
            thrown_numbers = []
            sense.show_message('Player 2 roll the dice 5 times', scroll_speed=0.05)
            player_2 = True
            player_1 = False
        # else if player_2 is true make total sum of numbers in array for player 2
        # empty array
        # show scores of both players
        # wait for 5 seconds before resetting everything
        elif player_2:
            player_2_score = sum(thrown_numbers)
            thrown_numbers = []
            sense.show_message('Player 1 your score is {0} Player 2 your score is {1}'.format(player_1_score, player_2_score), scroll_speed=0.05)
            sleep(5)
            main()

def roll_dice():
    number = randint(1, 6)
    #display the random number on the led display
    sense.show_letter(str(number), text_colour=black, back_colour=white)
    # add the random number to the array
    add_score(number)

def track_movement():
    print('tracking movement')
    while True:
        # get initial values of accelerometer
        x, y, z = sense.get_accelerometer_raw().values()
        
        # set variables to absolute value
        x1 = abs(x)
        y1 = abs(y)
        z1 = abs(z)
        
        if x1 > 2 or y1 > 2 or z1 > 2:
            roll_dice()
            
try:
    sense = SenseHat()
    sense.set_imu_config(False, False, True)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)

def main():
    sense.show_message("Player 1, roll the dice 10 times", scroll_speed=0.05)
    sense.clear()
    player_1 = True
    track_movement()
    
        
if __name__ == "__main__":
    try:
        main()
    except(KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sys.exit(0)