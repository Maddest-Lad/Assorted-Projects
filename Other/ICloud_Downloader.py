import pydirectinput as pdt
from time import sleep

sleep(5)

while True:
    # Start Bulk Selection
    pdt.keyDown("shift")

    # 50 Image Chunk
    for i in range(1, 50):
        pdt.press("up")

    # End Bulk Selection
    pdt.keyUp("shift")

    # Click Download
    pdt.leftClick(3886, 120)
    sleep(2)

    # Select New Start Photo
    pdt.press("left")
    sleep(1)


