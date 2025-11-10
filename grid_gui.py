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

def grid_apply(grid):
    return

def grid_reset(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            grid[row][col].reset()

    return

def grid_status_in_text(grid):
    text = ""
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col].is_on:
                text += "0"
            else:
                text += "-"
        text += "\n"
    print(text)
    return 


class GridSquare:
    def __init__(self, root):
        self.root = root
        self.is_on = False
        self.is_solved = False
        
        self.button = tk.Button(
            root,
            bg = TOGGLE_OFF_GRID_BG,
            fg = TOGGLE_OFF_GRID_FG,
            activebackground=TOGGLE_OFF_GRID_BG,
            activeforeground=TOGGLE_OFF_GRID_FG,
            bd = 2,
            highlightthickness=0,
            relief=tk.RAISED,
            command = self.toggle_state
        )

    def toggle_state(self):
        if self.is_on:
            #turn button off
            self.button.config(bg=TOGGLE_OFF_GRID_BG, 
                               fg=TOGGLE_OFF_GRID_FG,
                               activebackground=TOGGLE_OFF_GRID_BG,
                               activeforeground=TOGGLE_OFF_GRID_FG)
        else:
            #turn button on
            self.button.config(bg=TOGGLE_ON_GRID_BG,
                               fg=TOGGLE_ON_GRID_FG,
                               activebackground=TOGGLE_ON_GRID_BG,
                               activeforeground=TOGGLE_ON_GRID_FG)
        
        #toggle state
        self.is_on = not self.is_on
        return
    
    def reset(self):
        self.is_on = False
        self.is_solved = False
        self.button.config(bg=TOGGLE_OFF_GRID_BG, 
                               fg=TOGGLE_OFF_GRID_FG,
                               activebackground=TOGGLE_OFF_GRID_BG,
                               activeforeground=TOGGLE_OFF_GRID_FG)
