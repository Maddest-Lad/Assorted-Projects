from time import sleep

import pydirectinput as dirt


if __name__ == '__main__':

    while True:
        # Move To Slab & Start Watering
        dirt.moveTo(x=960, y=612)
        dirt.mouseDown(button="right")
        sleep(13)

        # Release Mouse
        dirt.rightClick()

        # Refill At Sink
        dirt.moveTo(x=960, y=450)
        dirt.rightClick()

