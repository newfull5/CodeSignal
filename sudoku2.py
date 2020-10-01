import numpy as np

def Check(array):
    temp = list(''.join(array.flatten().tolist()).replace('.',''))
    return len(temp) == len(set(temp))
    
def sudoku2(grid):
    grid = np.array(grid)

    grids = [grid[:3,:3],
    grid[:3,3:6],
    grid[:3,6:],
    grid[3:6,:3],
    grid[3:6,3:6],
    grid[3:6,6:],
    grid[6:,:3],
    grid[6:,3:6],
    grid[6:,6:]]

    for g in grids:
        if not Check(g):
            return False
        
    for i in range(9):
        if not Check(grid[:,i]):
            return False
        
        if not Check(grid[i,:]):
            return False
    return True
