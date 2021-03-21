from time import sleep

import pydirectinput as dirt
from PIL import ImageGrab

# Global Colors For The Fishing Bobber
ABOVE_WATER = [242, 251, 58]
BELOW_WATER = [100, 134, 109]


# Determines The Closeness of Two RGB Colors, Using t or Threshold As The Deciding Factor
def similar_colors(color_1: list, color_2: list, t: int) -> bool:
    return abs(color_1[0] - color_2[0]) + abs(color_1[1] - color_2[1]) + abs(color_1[2] - color_2[2]) < t


# Captures The Colors In An Area of The Screen And Returns True If One of the Colors Matches the BELOW_WATER Bobber
def fish_bitting() -> bool:
    capture = ImageGrab.grab(bbox=(940, 200, 1000, 700))  # Left, Upper, Right, Lower

    # Remove Alpha (Transparency) Values From The Color List
    colors = [i for i in capture.quantize(colors=16, method=2).getpalette() if i != 0]

    # Split Color List Into Sublists That Are Each 3 Elements Long
    color_list = [colors[i * 3:(i + 1) * 3] for i in range((len(colors) + 3 - 1) // 3)]

    # Check For Color Similarity
    for i in color_list:
        if len(i) == 3:
            if similar_colors(BELOW_WATER, i, 5):
                print(i, BELOW_WATER)
                return True

    return False


if __name__ == '__main__':

    while True:

        if fish_bitting():
            # Reel In
            dirt.rightClick()
            sleep(1)

            # Recast
            dirt.rightClick()
            sleep(3)
