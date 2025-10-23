import tkinter as tk
from constants import *

# Function for initialising the main grid and the array to store the grid states
def grid_setup(root):   
    return GridSquare(root)

# Function for toggling the grid square between on and off
def toggle_grid_square():
    return

class GridSquare:
    def __init__(self, root):
        self.root = root
        self.is_on = False
        




        self.button = tk.Button(
            root,
            bg = TOGGLE_OFF_BG,
            fg = TOGGLE_OFF_FG,
            relief=tk.RAISED,
            command = self.toggle_state
        )

    def toggle_state(self):
        if self.is_on:
            #turn button off
            self.button.bg = TOGGLE_OFF_BG
            self.button.fg = TOGGLE_OFF_FG
        else:
            #turn button on
            self.button.bg = TOGGLE_ON_BG
            self.button.fg = TOGGLE_ON_FG
        
        #toggle state
        self.is_on = not self.is_on
        return
