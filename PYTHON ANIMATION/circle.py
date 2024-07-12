import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()

# Set axis limits
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Create a point
point, = ax.plot([], [], 'ro')

# Initialization function: plot the background of each frame
def init():
    point.set_data([], [])
    return point,

# Animation function: this is called sequentially
def animate(i):
    angle = np.radians(i)  # Convert degrees to radians
    x = np.cos(angle)
    y = np.sin(angle)
    point.set_data(x, y)
    return point,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=50, blit=True)

# Show the animation
plt.show()
