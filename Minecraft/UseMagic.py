import pydirectinput as dit
from time import sleep

CLICK_TIME = 26
RECHARGE_TIME = 64

sleep(5)

while True:

    dit.mouseDown(button="right")

    sleep(CLICK_TIME)

    dit.mouseUp(button="right")

    sleep(RECHARGE_TIME)

