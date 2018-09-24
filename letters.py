from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

dark_green = (0, 102, 0)
orange = (255, 128, 0)

word = input ("Choose a word to display: ")
speed = int(input("Choose how many seconds are between each letter: "))
string_array = list(word)

    
try:
    sense = SenseHat()
    sense.set_imu_config(False, False, True)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)

def main():
    while True:
      for x in string_array:
        sense.show_letter(x, text_colour = orange, back_colour = dark_green)
        sleep(speed)
    
        
if __name__ == "__main__":
    try:
        main()
    except(KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sys.exit(0)
