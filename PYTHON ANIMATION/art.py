import pygame # type: ignore
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Graphics Animation")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the rectangle
rect_width, rect_height = 50, 50
rect_x, rect_y = 0, height // 2 - rect_height // 2
rect_speed = 5

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Update the position of the rectangle
    rect_x += rect_speed
    if rect_x > width:
        rect_x = -rect_width

    # Draw the rectangle
    pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
sys.exit()
