import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def hexagon_points(radius, num_points):
    """Generate the vertices of a hexagon."""
    angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    points = np.array([[np.cos(angle), np.sin(angle)] for angle in angles])
    return radius * points

def update(frame, lines, hex_points, num_lines):
    for i, line in enumerate(lines):
        rotation_angle = np.deg2rad(frame + i * (360 / num_lines))
        rotation_matrix = np.array([
            [np.cos(rotation_angle), -np.sin(rotation_angle)],
            [np.sin(rotation_angle), np.cos(rotation_angle)]
        ])
        rotated_points = hex_points @ rotation_matrix.T
        line.set_data(rotated_points[:, 0], rotated_points[:, 1])
    return lines

def create_animation():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')

    num_lines = 6
    hex_radius = 1.0
    hex_points = hexagon_points(hex_radius, num_lines)
    colors = plt.cm.rainbow(np.linspace(0, 1, num_lines))

    lines = [ax.plot([], [], color=color, lw=2)[0] for color in colors]

    ani = animation.FuncAnimation(fig, update, frames=360, fargs=(lines, hex_points, num_lines), interval=20, blit=True)

    plt.show()

create_animation()
