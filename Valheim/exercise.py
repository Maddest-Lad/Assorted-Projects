import pydirectinput as pdt
from time import sleep

sleep(3)

# pdt.press("ctrl")
while True:
    # # Sneak
    # pdt.keyDown("w")
    # sleep(16)
    # pdt.keyUp("w")
    # sleep(7)

    # Run
    pdt.keyDown("shift")
    pdt.keyDown("w")
    sleep(7)
    pdt.keyUp("w")
    pdt.keyUp("shift")
    sleep(2.3)

    # # Jump
    # sleep(1)
    # pdt.press("space")
    # sleep(1)
    # pdt.press("space")
    # sleep(1)
    # pdt.press("space")
    # sleep(1)
    # pdt.press("space")
    # sleep(1)
    # pdt.press("space")
    # sleep(1)
    # pdt.press("space")
    # sleep(2.3)