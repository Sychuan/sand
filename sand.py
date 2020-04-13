import numpy as np
import matplotlib.pyplot as plt
import time



# size of grid
xsize = 900
ysize = 900
random_grid_flag = False

if not random_grid_flag:
    # initializing grid with zeros
    grid = np.zeros((xsize, ysize), dtype=np.int)
    # or random initialization
else:
    grid = np.random.randint(0, 6, (xsize, ysize))

# generating sand
grid[450, 450] = 100000

# finding unstable sand piles
unstable_sand = np.argwhere(grid >= 4)

# defining step
def step(grid, sands):
    #removing 4 sands from unstable
    grid[sands[:, 0], sands[:, 1]] -= 4
    grid[(sands[:, 0]+1)%xsize, sands[:, 1]] += 1
    grid[(sands[:, 0] - 1) % xsize, sands[:, 1]] += 1
    grid[sands[:, 0] , (sands[:, 1]+1)%ysize] += 1
    grid[sands[:, 0] , (sands[:, 1]-1)%ysize] += 1
    #adding removed to adjacent cells
    '''grid = np.roll(grid,1, axis=0)
    grid[sands[:, 0], sands[:, 1]] += 1
    grid = np.roll(grid,-2, axis=0)
    grid[sands[:, 0], sands[:, 1]] += 1
    grid = np.roll(grid, 1, axis=0)

    grid = np.roll(grid, 1, axis=1)
    grid[sands[:, 0], sands[:, 1]] += 1
    grid = np.roll(grid, -2, axis=1)
    grid[sands[:, 0], sands[:, 1]] += 1
    grid = np.roll(grid, 1, axis=1)'''

    return grid

start = time.time()

# while some piles are unstable do steps
while len(unstable_sand) > 0:
    unstable_sand = np.argwhere(grid >= 4)
    if len(unstable_sand) > 0:
        grid = step(grid, unstable_sand)
end = time.time()
print("time: ", end - start)
# saving image
plt.imshow(grid)
plt.imsave("exp1.png", grid, cmap="gray")
plt.close()
print("fin")
