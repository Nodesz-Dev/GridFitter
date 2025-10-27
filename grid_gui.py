import tkinter as tk
from constants import *

# Function for initialising the main grid and the array to store the grid states
def grid_setup(root): 
    grid = []

    for row in range(MAIN_GRID_HEIGHT):
        col_array = []
        for col in range(MAIN_GRID_WIDTH):
            new_sqr = GridSquare(root)
            new_sqr.button.grid(row=row,column=col)
            col_array.append(new_sqr)
            
        grid.append(col_array)

    return grid

class GridSquare:
    def __init__(self, root):
        self.root = root
        self.is_on = False
        self.is_solved = False
        
        self.button = tk.Button(
            root,
            bg = TOGGLE_OFF_BG,
            fg = TOGGLE_OFF_FG,
            activebackground=TOGGLE_OFF_BG,
            activeforeground=TOGGLE_OFF_FG,
            bd = 2,
            highlightthickness=0,
            relief=tk.RAISED,
            command = self.toggle_state
        )

    def toggle_state(self):
        print("button clicked")
        if self.is_on:
            #turn button off
            self.button.config(bg=TOGGLE_OFF_BG, 
                               fg=TOGGLE_OFF_FG,
                               activebackground=TOGGLE_OFF_BG,
                               activeforeground=TOGGLE_OFF_FG)
            print("turning off")
        else:
            #turn button on
            self.button.config(bg=TOGGLE_ON_BG,
                               fg=TOGGLE_ON_FG,
                               activebackground=TOGGLE_ON_BG,
                               activeforeground=TOGGLE_ON_FG)
            print("turning on")
        
        #toggle state
        self.is_on = not self.is_on
        print(f"button is now {self.is_on}")
        return
    
    def reset(self):
        self.is_on = False
        self.is_solved = False
        self.button.config(bg=TOGGLE_OFF_BG, 
                               fg=TOGGLE_OFF_FG,
                               activebackground=TOGGLE_OFF_BG,
                               activeforeground=TOGGLE_OFF_FG)
