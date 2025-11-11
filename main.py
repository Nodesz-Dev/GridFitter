import tkinter as tk
from grid_gui import *
from engines import *

def main():
    root = setup_main_window()
    setup_engine_and_component_menu_window(root)
    

    root.mainloop()

def setup_main_window():
    main_window_root = tk.Tk()
    global GLOBAL_Main_Grid
    GLOBAL_Main_Grid[:] = grid_setup(main_window_root)

    clear_button = tk.Button(main_window_root, text="Clear",command=lambda:grid_reset())
    clear_button.grid(row=MAIN_GRID_CLEAR_HEIGHT_POSITION, column=MAIN_GRID_CLEAR_WIDTH_POSITION)

    debug_text_button = tk.Button(main_window_root, text="Debug text", command=lambda:grid_status_in_text(GLOBAL_Main_Grid))
    debug_text_button.grid(row=MAIN_GRID_DEBUG_BUTTON_HEIGHT_POSITION,column=MAIN_GRID_DEBUG_BUTTON_WIDTH_POSITION)

    return main_window_root

def setup_engine_and_component_menu_window(root):
    engine_menu_window_root = tk.Toplevel(root)

    # Reactor Menu setup
    reactor_dropdown_setup(engine_menu_window_root)

    # Generator menu setup
    generator_dropdown_setup(engine_menu_window_root)


if __name__ == '__main__':
        main()