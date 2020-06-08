# DK '23
# This is an epidemic simulator for Epidemic Day

import Functions  # Import functions from other file
import PySimpleGUI as sg  # Import PySimpleGUI
import random as rnd  # Import random

# Options for the size of the grid of people (squares from 5 to 30)
population_increments = [25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576,
                         625, 676, 729, 784, 841, 900]
# Define variables to store simulation variables.
population, infection_rate, recovery_rate, recovery_rate_increase, fatality_rate, fatality_rate_decrease = 0, 0, 0, 0, \
                                                                                                           0, 0
entity_map = []  # Define 2D array of entities

# Define the starting layout of the PySimpleGUI window
layout = [[sg.T("Welcome to the Epidemic Day Epidemic Simulation", font=("Lucida Grande", 18))],
          [sg.Slider(range=(5, 30), orientation="h", default_value=14, key="population", disable_number_display=True,
                     size=(40, 15)),
           sg.T("Population (25 - 900)")],
          [sg.Slider(range=(1, 100), orientation="h", default_value=10, key="infection_rate", size=(40, 15)),
           sg.T("Infection rate (1% to 100%)")],
          [sg.Slider(range=(0, 100), orientation="h", default_value=60, key="recovery_rate", size=(40, 15)),
           sg.T("Recovery rate (1% to 100%)")],
          [sg.Checkbox("Should recovery rate increase?", default=False, key="RRI"), sg.VerticalSeparator(pad=None),
           sg.T("Rate will increase at"), sg.Input(size=(3, 1), key="RIP"), sg.T("percent per cycle.")],
          [sg.Slider(range=(0, 100), orientation="h", default_value=5, key="fatality_rate", size=(40, 15)),
           sg.T("Fatality rate (1% - 100%)")],
          [sg.Checkbox("Fatality rate decreasing at", default=False, key="FRD"),
           sg.Input(size=(3, 1), key="FDP"), sg.T("percent per cycle.")],
          [sg.Button("Start Simulation"), sg.Button("Exit")]]

# noinspection PyUnresolvedReferences
#if __name__ == "__main__":
starting_window = sg.Window("Epidemic Simulation", layout)  # Start PySimpleGUI window
# Loop to check for events within the PySimpleGUI window
while True:
    event, values = starting_window.Read()  # Read values
    if event == "Start Simulation":  # If start event
        # Set values for variables received from input window
        population, infection_rate, recovery_rate, fatality_rate = values["population"]**2, \
                                                                   values["infection_rate"] / 100, \
                                                                   values["recovery_rate"] / 100, \
                                                                   values["fatality_rate"] / 100
        if values["RRI"]:
            recovery_rate_increase = float(values["RIP"]) / 100
        else:
            recovery_rate_increase = 0
        if values["FRD"]:
            fatality_rate_decrease = float(values["FDP"]) / 100
        else:
            fatality_rate_decrease = 0
        # Set coordinate plane variable to output from function
        entity_map = Functions.createCoordinatePlane(population)
        # Set one of the people to infected status ("I")
        entity_map[rnd.randint(0, len(entity_map) - 1)][rnd.randint(0, len(entity_map) - 1)] = "I  "
        # Functions.printEntityMap(entity_map)
        break  # Break out of infinite loop
    if event is None or "Exit":  # If exit event
        quit()  # Break out of infinite loop
starting_window.close()  # Close starting window

import Pyglet_window