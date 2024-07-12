import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
box_width = 10
box_height = 5
ball_radius = 0.5
initial_position = [5, 4]  # Initial position of the ball
initial_velocity = 0.1      # Initial velocity of the ball
direction_x = 1             # Initial direction of the ball in the x-axis
direction_y = 1             # Initial direction of the ball in the y-axis

# Create a figure and axis
fig, ax = plt.subplots()

# Set axis limits
ax.set_xlim(0, box_width)
ax.set_ylim(0, box_height)

# Create a ball object
ball = plt.Circle(initial_position, ball_radius, fc='r')

# Add the ball to the axis
ax.add_patch(ball)

# Update function for the animation
def update(frame):
    global direction_x, direction_y
    # Update ball position
    x, y = ball.center
    x += initial_velocity * direction_x  # Move the ball horizontally
    y += initial_velocity * direction_y  # Move the ball vertically
    ball.center = (x, y)
    
    # Check if the ball reaches the boundaries
    if x <= ball_radius or x >= box_width - ball_radius:
        direction_x *= -1  # Reverse the direction in the x-axis
    if y <= ball_radius or y >= box_height - ball_radius:
        direction_y *= -1  # Reverse the direction in the y-axis
    
    return ball,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()
