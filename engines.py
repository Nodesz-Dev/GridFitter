import tkinter as tk
from constants import *
from engine_constants import *

def reactor_dropdown_setup(root):
    selected_option = tk.StringVar()
    selected_option.set(REACTOR_OPTIONS[0])

    label = tk.Label(root, text=REACTOR_DROPDOWN_LABEL)
    label.grid(row=1,column=1)

    dropdown = tk.OptionMenu(root, selected_option, *REACTOR_OPTIONS)
    dropdown.config(width=ENGINE_COMPONENT_DROPDOWN_WIDTHS)
    dropdown.grid(row=1,column=2)

    def reactor_on_select(var, index, mode, reactor_options=REACTOR_OPTIONS):
    
        print(f"variable: {selected_option.get()}")
        print(f"index: {index}")
        print(f"variable: {mode}")
        return

    selected_option.trace_add("write", reactor_on_select)

    return 



def generator_dropdown_setup(root, gen=1):
    selected_option = tk.StringVar()
    selected_option.set(GENERATOR_OPTIONS[0])

    if gen == 1:
        label = tk.Label(root, text=GENERATOR_DROPDOWN_LABEL_FIRST)
        label.grid(row=2,column=1)
        dropdown = tk.OptionMenu(root, selected_option, *GENERATOR_OPTIONS)
        dropdown.config(width=ENGINE_COMPONENT_DROPDOWN_WIDTHS)
        dropdown.grid(row=2,column=2)
        generator_dropdown_setup(root, gen=2)
    elif gen == 2:
        label = tk.Label(root, text=GENERATOR_DROPDOWN_LABEL_SECOND)
        label.grid(row=3,column=1)
        dropdown = tk.OptionMenu(root, selected_option, *GENERATOR_OPTIONS)
        dropdown.config(width=ENGINE_COMPONENT_DROPDOWN_WIDTHS)
        dropdown.grid(row=3,column=2)

    def reactor_on_select(var, index, mode, generator=gen, generator_options=GENERATOR_OPTIONS):
    
        print(f"variable: {selected_option.get()}")
        print(f"index: {index}")
        print(f"variable: {mode}")
        print(f"Gen num: {generator}")
        return

    selected_option.trace_add("write", reactor_on_select)

    return 