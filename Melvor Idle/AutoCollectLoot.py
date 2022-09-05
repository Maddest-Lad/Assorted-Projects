from time import sleep

import pyautogui as auto

# Auto Collect Loot From Fighting

while True:
    auto.hscroll(-1000)
    sleep(1)
    for i in range(0, 150, 15):
        auto.moveTo(x=1794, y=751 + i)
    sleep(30)
