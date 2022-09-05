import pydirectinput as pdt
from time import sleep

# locations
dough_corner = (1149, 684)
crafting_grid_plus = (1202, 417)
output_slot = (1052, 548)
terminal = (931, 323)

sleep(4)
while True:
    pdt.moveTo(*dough_corner)
    sleep(0.25)r
    pdt.press("r")
    sleep(0.25)
    pdt.leftClick(*crafting_grid_plus)
    sleep(0.25)
    pdt.leftClick(*output_slot)
    sleep(0.25)
    pdt.leftClick(*terminal)
    sleep(0.75)
