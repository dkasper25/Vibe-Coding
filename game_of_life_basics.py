import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np



rng = np.random.default_rng()


def initialize_grid(size, percent_one):
    return np.random.choice([0, 1], size=(size, size), p=[1 - percent_one, percent_one])

def update(grid):
    new_grid = np.copy(grid)
    neighbours = [(-1,0), (1,0), (0,1), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]
    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            count = 0
            for dx, dy in neighbours:
                count += grid[i + dx, j + dy]
            if grid[i, j] == 1 and (count < 2 or count > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and count == 3:
                new_grid[i, j] = 1
    return new_grid

# Initialize
size = 200
grid = initialize_grid(size, 0.09)

fig, ax = plt.subplots(figsize = (100,100))
img = ax.imshow(grid, cmap='gray', interpolation='nearest')
ax.set_xticks([]), ax.set_yticks([])  # Removes ticks from graph to clean up
# Add a text object to update the iteration number
iteration_text = ax.text(0.02, 0.95, '', color='red', fontsize=12,
                         transform=ax.transAxes, ha='left', va='top')


#Animation update function
def animate(frame):
    global grid
    grid = update(grid)
    img.set_data(grid)
    iteration_text.set_text(f"Iteration: {frame}")
    return [img, iteration_text]

ani = animation.FuncAnimation(fig, animate, frames=200, interval=10, blit=True)
plt.show()

