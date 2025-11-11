import tkinter as tk
from constants import *
from globals import *
from engine_constants import *
from grid_gui import grid_apply

def reactor_dropdown_setup(root):
    selected_option = tk.StringVar()
    selected_option.set(REACTOR_OPTIONS[0])

    label = tk.Label(root, text=REACTOR_DROPDOWN_LABEL)
    label.grid(row=1,column=1)

    dropdown = tk.OptionMenu(root, selected_option, *REACTOR_OPTIONS)
    dropdown.config(width=ENGINE_COMPONENT_DROPDOWN_WIDTHS)
    dropdown.grid(row=1,column=2)

    def reactor_on_select(var, index, mode, reactor_options=REACTOR_OPTIONS):
        reactor_index = reactor_options.index(selected_option.get())
        apply_reactor_change(reactor_index)
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
        gen_index = generator_options.index(selected_option.get())
        apply_generator_change(gen_index, generator)
        return

    selected_option.trace_add("write", reactor_on_select)

    return 

def apply_reactor_change(index):
    tmp_reactor = REACTOR_ARRAYS[index].copy()
    GLOBAL_Current_Reactor[:] = tmp_reactor
    grid_apply()

def apply_generator_change(index, gen_num):
    tmp_gen = GENERATOR_ARRAYS[index].copy()
    if gen_num == 1:
        GLOBAL_Current_First_Generator[:] = tmp_gen
    elif gen_num == 2:
        GLOBAL_Current_Second_Generator[:] = tmp_gen

    grid_apply()