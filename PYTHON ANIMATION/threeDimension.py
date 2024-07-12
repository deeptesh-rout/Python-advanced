from vpython import *

# Create a 3D scene
scene = canvas(title='Rotating 3D Cube')

# Create a cube
cube = box(pos=vector(0, 0, 0), size=vector(2, 2, 2), color=color.blue)

# Rotation angles
angle_x = 0
angle_y = 0
angle_z = 0

# Animation loop
while True:
    rate(50)  # 50 frames per second
    angle_x += 0.01
    angle_y += 0.01
    angle_z += 0.01

    # Rotate the cube around its center
    cube.rotate(angle=0.01, axis=vector(1, 0, 0))
    cube.rotate(angle=0.01, axis=vector(0, 1, 0))
    cube.rotate(angle=0.01, axis=vector(0, 0, 1))

