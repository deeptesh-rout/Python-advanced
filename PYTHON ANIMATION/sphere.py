from vpython import *

# Create a 3D scene
scene = canvas(title='3D Bouncing Ball')

# Create a ball
ball = sphere(pos=vector(0, 5, 0), radius=1, color=color.red, make_trail=True)

# Create the ground
ground = box(pos=vector(0, -0.5, 0), size=vector(10, 1, 10), color=color.green)

# Initial velocity and acceleration
ball.velocity = vector(0, -1, 0)
g = vector(0, -9.8, 0)  # Gravity

# Time step
dt = 0.01

# Animation loop
while True:
    rate(100)  # 100 frames per second
    ball.velocity = ball.velocity + g * dt
    ball.pos = ball.pos + ball.velocity * dt

    # Check for collision with the ground
    if ball.pos.y < ball.radius:
        ball.velocity.y = -ball.velocity.y  # Reverse the velocity

