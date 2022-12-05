import time

import pydirectinput as pdt

# Scanning
while True:
    time.sleep(1)
    print(pdt.position())

# Setup


# while True:
#     # Click Ad Blimp

#     time.sleep(30)  # Let Ad Play for 30 Seconds
#     pdt.leftClick((1785, 212))
#     time.sleep(5)  # In Case They Have Multiple Ads
#     pdt.leftClick((1785, 212))
#
#     # After Ad, Collect Reward
#     pdt.leftClick((1772, 222))  # Chat Icon
#     pdt.leftClick((1465, 396))  # Inbox Tab
#     pdt.leftClick((1615, 921))  # Collect Button
#     pdt.press("esc")  # Close Chat
