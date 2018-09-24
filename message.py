from sense_hat import SenseHat
import os
import sys
sense = SenseHat()

blue = (0, 0, 225)
yellow = (255, 255, 0)
    
try:
    sense = SenseHat()
    sense.set_imu_config(False, False, True)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)

def main():
    while True:
        sense.show_message("Hello! We are New Media Development :)", text_colour=yellow, back_colour=blue)
        
if __name__ == "__main__":
    try:
        main()
    except(KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sys.exit(0)