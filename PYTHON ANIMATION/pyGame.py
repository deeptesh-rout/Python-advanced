import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Animation")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the square
square_size = 50
square_color = WHITE
square_x = width // 2 - square_size // 2
square_y = height // 2 - square_size // 2
speed_x = 5
speed_y = 3

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the square
    square_x += speed_x
    square_y += speed_y

    # Check boundaries
    if square_x <= 0 or square_x + square_size >= width:
        speed_x *= -1
    if square_y <= 0 or square_y + square_size >= height:
        speed_y *= -1

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the square
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
