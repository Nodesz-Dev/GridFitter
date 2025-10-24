import tkinter as tk
from grid_gui import *

def main():
    root = tk.Tk()
    root.geometry('1400x900')
    main_grid_states = grid_setup(root)
    root.mainloop()

main()