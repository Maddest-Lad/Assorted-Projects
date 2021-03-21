from time import sleep

import pydirectinput as auto

# Open A Chrome
auto.leftClick(464, 1059)
sleep(1)

# Open A New Tab
auto.keyDown('ctrl')
auto.typewrite('n')
auto.keyUp('ctrl')

# Go To The Site
auto.write('https')
auto.keyDown('shift')
auto.write(';')
auto.keyUp('shift')
auto.write('//dailyhealth.rit.edu/')
auto.press('enter')
sleep(1)

# Enter Site
auto.leftClick(296, 438)
sleep(1)

# Click No
auto.leftClick(991, 632)
sleep(1)

# Close Site
auto.keyDown('ctrl')
auto.typewrite('w')
auto.keyUp('ctrl')
