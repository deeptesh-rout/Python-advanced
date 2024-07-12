import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Create figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate data for a 3D sine wave
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Create a plot object
plot = ax.plot_surface(x, y, z, cmap='viridis')

# Set up the axes properties
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-1, 1])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Function to update the plot
def update(frame):
    ax.view_init(elev=30, azim=frame)
    return plot,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(0, 360, 2), blit=False)

# Save the animation
ani.save('3d_sine_wave_rotation.gif', writer='imagemagick')

# Show the plot
plt.show()
