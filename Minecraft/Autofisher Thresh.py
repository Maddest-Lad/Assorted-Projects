from time import sleep
from RingBuffer import RingBuffer

import numpy as np
import pydirectinput as dirt
from PIL import ImageGrab
import scipy.ndimage as ndi

MOVING_AVERAGE = []


# Captures The Colors In An Area of The Screen And Returns True If One of the Colors Matches the BELOW_WATER Bobber
def get_center():
    capture = ImageGrab.grab(bbox=(956, 528, 1300, 730))  # Left, Upper, Right, Lower

    thresh = 40
    fn = lambda x: 255 if x > thresh else 0
    img = capture.convert('L').point(fn, mode='1')

    return ndi.center_of_mass(np.array(img))


if __name__ == '__main__':

    sleep(3)
    buffer = RingBuffer(64)
    buffer.append(get_center())

    while True:

        current = get_center()

        print(abs(buffer.average()[1] - current[1]))

        if abs(current[1] - buffer.average()[1]) > 0.055:
            # Reel In
            dirt.rightClick()
            sleep(1)

            # Recast
            dirt.rightClick()
            sleep(3)
        else:
            buffer.append(current)
            sleep(0.125)

