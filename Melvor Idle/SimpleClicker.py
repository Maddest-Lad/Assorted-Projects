import pyautogui as auto
from time import sleep

while True:
    auto.hscroll(-1000)
    sleep(1)
    for i in range(0, 150, 15):
        auto.click(x=1834, y=731+i)
    sleep(30)
