import tkinter as tk
from grid_gui import *

def main():
    root = tk.Tk()
    root.geometry('1400x900')
    main_grid = grid_setup(root)

    clear_button = tk.Button(root, text="Clear",command=lambda:clear_grid(main_grid))
    clear_button.grid(row=MAIN_GRID_CLEAR_HEIGHT_POSITION, column=MAIN_GRID_CLEAR_WIDTH_POSITION)

    debug_text_button = tk.Button(root, text="Debug text", command=lambda:grid_status_in_text(main_grid))
    debug_text_button.grid(row=MAIN_GRID_DEBUG_BUTTON_HEIGHT_POSITION,column=MAIN_GRID_DEBUG_BUTTON_WIDTH_POSITION)

    root.mainloop()

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

def clear_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            grid[row][col].reset()

    return

if __name__ == '__main__':
        main()