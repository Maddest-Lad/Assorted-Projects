import keyboard
import time
import os
import pyautogui as auto


class Automation:

    def __init__(self):

        # Screen Rez
        self.rez = auto.size()

        # Mining Stuff
        self.ore_positions = [(482, 550), (875, 550), (1298, 550), (1870, 550), (460, 850), (890, 850)]
        self.ore_names = ["Rune Essence", "Copper", "Tin", "Iron", "Coal", "Silver"]

    # Evenly Distributes Time Mining Ores, cycles to avoid ore depletion
    # mine_time : integer representing the seconds to mine for
    def mine(self, mine_time, verbose=None):

        # Select Mining Tab
        auto.moveTo(100, 500)
        auto.scroll(auto.size()[1] * 2)
        auto.click(x=30, y=932, button='left')

        end = time.time() + mine_time

        while end > time.time():

            for ore, name in zip(self.ore_positions, self.ore_names):

                if verbose:
                    print("Mining {} At {}".format(name, ore))

                auto.click(x=ore[0], y=ore[1], button='left')
                time.sleep(30)

    def fish(self, fish_time, verbose=None):

        # Select Fishing Tab
        auto.moveTo(100, 500)
        auto.scroll(10000)
        auto.click(x=30, y=820, button='left')

        # Move to Bottom Of Tab
        auto.moveTo(x=self.rez[0]/2, y=self.rez[1]/2)
        auto.vscroll(-1000)

        # Select Raw Swordfish & Start Fishing
        auto.click(x=464, y=752)
        auto.click(x=855, y=890)

        end = time.time() + fish_time

        while end > time.time():
            time.sleep(60)
            if verbose:
                print("Still Fishing")


    @staticmethod
    def print_position():

        while True:
            time.sleep(1)
            print(auto.position())


a = Automation()
a.mine(3600, True)
a.fish(3600, True)
# a.print_position()


