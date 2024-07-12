import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()

# Set axis limits
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-5, 5)

# Create a line object
line, = ax.plot([], [], lw=2)

# Initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# Animation function: this is called sequentially
def animate(i):
    x = np.linspace(0.01, 2*np.pi - 0.01, 1000)  # Avoid singularities at 0 and pi
    y = np.tan(x + 0.1*i)  # Tangent wave
    line.set_data(x, y)
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
