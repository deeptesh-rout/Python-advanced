from vpython import *

# Create a 3D scene
scene = canvas(title='Multiple Rotating Cubes', width=800, height=600)

# Create a list to hold the cubes
cubes = []

# Create and add multiple cubes to the list
num_cubes = 5
for i in range(num_cubes):
    cube = box(pos=vector(i * 3, 0, 0), size=vector(1, 1, 1), color=color.red)
    cubes.append(cube)

# Rotation angles
angles = [0] * num_cubes

# Animation loop
while True:
    rate(50)  # 50 frames per second

    # Update rotation angles for each cube
    for i in range(num_cubes):
        angles[i] += 0.01 * (i + 1)  # Vary rotation speed for each cube

        # Rotate the cube around its center
        cubes[i].rotate(angle=0.01 * (i + 1), axis=vector(1, 0.5, 0.2))

