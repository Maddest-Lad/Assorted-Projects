import sys
from time import sleep

import pydirectinput as pdt


# Mines The Block In Front of the Player
def mine():
    pdt.press('1')
    pdt.mouseDown(button='left')  # Start Mining
    sleep(0.4521)  # Stone Hammer, Cobblestone (0.45) Gravel, (0.35) Sand
    #sleep1(0.352)
    pdt.mouseUp(button='left')  # Stop Mining


# Places A Block In Front of the Player
def place(slot: int):
    pdt.press(str(slot))  # Selects The Block in Slot's Slot
    pdt.rightClick()  # Place


# Give User2 Time to Tab Back Into The Game
sleep(3)
while True:
    # Start Block Slots at 2
    count = 2

    # Place and Mine 64 Blocks
    for i in range(1, 64):
        mine()
        place(count)
    count += 1

    # Stop After Hotbar is Emptied
    if count >= 9:
        sys.exit()
