import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

# Set up colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up the paddle
PADDLE_WIDTH, PADDLE_HEIGHT = 150, 20  # Increased paddle size
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 50, PADDLE_WIDTH, PADDLE_HEIGHT)

# Set up the ball
BALL_RADIUS = 10
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [3, 3]  # Decreased ball speed

# Set up bricks
BRICK_WIDTH, BRICK_HEIGHT = 80, 30
bricks = []
for i in range(7):
    for j in range(5):
        brick = pygame.Rect(i * (BRICK_WIDTH + 10) + 35, j * (BRICK_HEIGHT + 10) + 50, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
running = True
game_over = False
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    if not game_over:
        # Move the paddle
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            paddle.x -= 8  # Increased paddle speed
            paddle.x = max(paddle.x, 0)  # Limit paddle to the left boundary
        if keys[K_RIGHT]:
            paddle.x += 8  # Increased paddle speed
            paddle.x = min(paddle.x, WIDTH - paddle.width)  # Limit paddle to the right boundary

        # Move the ball
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # Collision detection with walls
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed[0] = -ball_speed[0]
        if ball.top <= 0:
            ball_speed[1] = -ball_speed[1]

        # Collision detection with paddle
        if ball.colliderect(paddle):
            ball_speed[1] = -ball_speed[1]

        # Collision detection with bricks
        for brick in bricks:
            if ball.colliderect(brick):
                bricks.remove(brick)
                ball_speed[1] = -ball_speed[1]

        # Check if game is over
        if len(bricks) == 0:
            game_over = True

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)
    pygame.display.flip()

    # Pause for a while
    clock.tick(60)

# Automatically end the task after the game is over
pygame.quit()
