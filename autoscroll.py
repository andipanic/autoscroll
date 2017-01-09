#!/usr/bin/python

#
# Automates mouse wheel scroll based on fraction of second increments.
#   This file should be in your path
#   

from time import sleep
from os import system


def main():
    set_speed = get_speed() 
    current_speed = set_speed + .15 
    while True:
        current_speed = update_speed(current_speed, set_speed)
        try:
            # TODO: check to see if xdotool is installed and fail loudly!
            system('xdotool click 5')
            system('xdotool key Down')
            sleep(current_speed)
        except KeyboardInterrupt:
            print('Done!')
            break


def get_speed():
    # TODO: put .autoscroll (speed) file in config
    with open('/home/andy/bin/.autoscroll') as speed:
        set_speed = float(speed.read().strip())
    return set_speed


def update_speed(current_speed, set_speed):
    if current_speed > set_speed:
        current_speed -= .01 
    return current_speed 


if __name__ == "__main__":
    main()
