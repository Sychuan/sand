import numpy as np
import matplotlib.pyplot as plt

# size of grid
xsize = 500
ysize = 500
random_grid_flag = False

if not random_grid_flag:
    # initializing grid with zeros
    grid = np.zeros((xsize, ysize), dtype=np.int)
    # or random initialization
else:
    grid = np.random.randint(0, 6, (xsize, ysize))

# generating sand
grid[500, 500] = 10000

# finding unstable sand piles
unstable_sand = np.argwhere(grid >= 4)

# defining step
def step(grid, sands):
    #removing 4 sands from unstable
    grid[sands[:, 0], sands[:, 1]] -= 4
    #adding to adjacent cells
    grid = np.roll(grid,1, axis=0)
    grid[sands[:, 0], sands[:, 1]] += 1
    grid = np.roll(grid,-2, axis=0)
    grid[sands[:, 0], sands[:, 1]] += 1
    grid = np.roll(grid, 1, axis=0)

    grid = np.roll(grid, 1, axis=1)
    grid[sands[:, 0], sands[:, 1]] += 1
    grid = np.roll(grid, -2, axis=1)
    grid[sands[:, 0], sands[:, 1]] += 1
    grid = np.roll(grid, 1, axis=1)

    return grid


# while some piles are unstable do steps
while len(unstable_sand) > 0:
    unstable_sand = np.argwhere(grid >= 4)
    if len(unstable_sand) > 0:
        grid = step(grid, unstable_sand)

# saving image
plt.imshow(grid)
plt.imsave("exp1.png", grid, cmap="gray")
plt.close()
print("fin")
