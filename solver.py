import globals as gl
from components import *
from grid_gui import grid_apply_solved, grid_to_int_array

def solver_handler():
    gl.GLOBAL_SOLVER_BEST_CASE_BLOCK_NUM = 0
    Component_list_creator()
    solve_packing(grid_to_int_array(gl.GLOBAL_Main_Grid), gl.GLOBAL_COMPONENT_LIST)
    grid_apply_solved()
    return

def place_block(grid, block, row, column, block_id):
    for r in range(len(block)):
        for c in range(len(block[r])):
            if block[r][c] == 1:
                if grid[r+row][c+column] != 1:
                    raise Exception(f"Cant place block, grid space already filled {block_id} at row {row}, column {column}")
                grid[r+row][c+column] = block_id
    return

def remove_block(grid, block, row, column, block_id):
    for r in range(len(block)):
        for c in range(len(block[r])):
            if block[r][c] == 1:
                if grid[r+row][c+column] != block_id:
                    raise Exception(f"Can't remove block, block id does not match the block being removed {block_id} at row {row}, column {column}")
                grid[r+row][c+column] = 1

    return

def is_valid_placement(grid, block_shape, row, col):
    """Check if a block can be placed at a specific row, col, avoiding obstacles."""
    grid_height = len(grid)
    grid_width = len(grid[0]) # Ensure it uses the width of the inner list
    block_height = len(block_shape)
    block_width = len(block_shape[0])

    if row + block_height > grid_height or col + block_width > grid_width:
        return False # Out of bounds

    for r in range(block_height):
        for c in range(block_width):
            grid_row = row + r
            grid_col = col + c
            # Check for overlap with existing shapes (marked > 1) or obstacles (marked == 0)
            if block_shape[r][c] == 1:
                if grid[grid_row][grid_col] != 1: 
                    return False # Overlap with placed block or obstacle
    return True

def check_for_best_case(grid, block_count):
    if block_count > gl.GLOBAL_SOLVER_BEST_CASE_BLOCK_NUM:
        gl.GLOBAL_SOLVER_BEST_CASE_BLOCK_NUM = block_count
        gl.GLOBAL_SOLVER_BEST_CASE_GRID[:] = [row.copy() for row in grid]

def solve_packing(grid=None, comp_list=None, current_block_count=0):
    if grid==None:
        raise Exception("No grid given to solver function")

    if comp_list==None:
        comp_list = []

    # Prune this branch if even placing all remaining components
    # cannot exceed the best solution found so far.
    if current_block_count + len(comp_list) <= gl.GLOBAL_SOLVER_BEST_CASE_BLOCK_NUM:
        return False

    check_for_best_case(grid, current_block_count)
    found_placement = False

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != 1:
                continue

            for component in comp_list:
                for shape in component.rotations:
                    if is_valid_placement(grid, shape, r, c):
                        found_placement = True
                        place_block(grid, shape, r, c, component.id)
                        new_block_list = comp_list.copy()
                        new_block_list.remove(component)
                        solve_packing(grid, new_block_list, current_block_count+1)
                        remove_block(grid, shape, r, c, component.id)

    return found_placement