import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the road path (a sine wave)
x_values = np.linspace(0, 10, 1000)
y_values = np.sin(x_values)

# Constants
car_length = 0.5  # Length of the car
car_speed = 0.05  # Speed of the car
initial_position = [0, np.sin(0)]  # Initial position of the car

# Create a figure and axis
fig, ax = plt.subplots()

# Set axis limits
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)

# Plot the road
ax.plot(x_values, y_values, 'b-')

# Create a rectangle representing the car
car_rect = plt.Rectangle(initial_position, car_length, 0.2, fc='r')

# Add the car to the axis
ax.add_patch(car_rect)

# Update function for the animation
def update(frame):
    global initial_position
    x, y = initial_position
    x += car_speed
    y = np.sin(x)
    car_rect.set_xy([x, y - 0.1])  # Update the car position
    initial_position = [x, y]  # Update the initial position
    return car_rect,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()
