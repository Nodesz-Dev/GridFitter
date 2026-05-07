from component_constants import *
import globals as gl

# Get selected components and create a list which is returned
# PLACEHOLDER CODE UNTIL COMPONENT SELECTOR UI IS CREATED
def get_selected_components():
    selected = []
    selected.append(SAMPLE_COMP_1)
    selected.append(SAMPLE_COMP_2)
    selected.append(SAMPLE_COMP_3)
    selected.append(SAMPLE_COMP_1)
    selected.append(SAMPLE_COMP_2)
    selected.append(SAMPLE_COMP_3)
    return selected

# take a list of arrays that represent components, get all possible rotations of the shape and convert them to a component object before returning
# as a new component list
def Component_list_creator():
    initial_component_array_list = get_selected_components()
    component_list = []
    id = 2 # start at 2 as 0 and 1 are reserved for empty and obstacle grid spaces respectively
    for array in initial_component_array_list:
        rotations = get_rotations(array)
        component = convert_to_component(id, rotations)
        component_list.append(component)
        id += 1
    gl.GLOBAL_COMPONENT_LIST[:] = component_list.copy()
    return gl.GLOBAL_COMPONENT_LIST

# convert a component array and its given id to a component object
def convert_to_component(id, block_rotations):
    tmp = Component(id, block_rotations)
    return tmp

# Take an array and return a list of arrays that represent all possible rotations of the original shape
def get_rotations(original_array):
    rotations_list = []
    rotations_list.append(original_array)
    loop_break = False
    rotated = original_array

    while not loop_break:
        rotated = rotate_clockwise(rotated)
        if rotated == original_array:
            loop_break = True
        else:
            rotations_list.append(rotated)
    return rotations_list

def rotate_clockwise(array):
    rotation = [list(row) for row in zip(*array[::-1])]
    return rotation
            
class Component:
    def __init__(self, id, block_rotations):
        self.id = id
        self.rotations = block_rotations

    # get currently chosen components array and return them as a list
    def get_components(self):
        return self.rotations
    
    def get_id(self):
        return self.id

    