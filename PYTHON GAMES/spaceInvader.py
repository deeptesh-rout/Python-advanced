import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
player_image = pygame.image.load('player.png')
enemy_image = pygame.image.load('enemy.png')
bullet_image = pygame.image.load('bullet.png')

# Player
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - 70
player_x_change = 0
player_speed = 1.5  # Adjusted player speed

# Enemy
enemy_x = random.randint(0, SCREEN_WIDTH - 64)
enemy_y = random.randint(50, 150)
enemy_x_change = 50  # Adjusted enemy speed
enemy_y_change = 40

# Bullet
bullet_x = 0
bullet_y = player_y
bullet_y_change = 5
bullet_state = "ready"

# Score
score = 0
font = pygame.font.SysFont("monospace", 35)

def show_score():
    text = "Score: " + str(score)
    label = font.render(text, 1, WHITE)
    SCREEN.blit(label, (10, 10))

def player(x, y):
    SCREEN.blit(player_image, (x, y))

def enemy(x, y):
    SCREEN.blit(enemy_image, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    SCREEN.blit(bullet_image, (x + 16, y + 10))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    if distance < 27:
        return True
    else:
        return False

# Game loop
running = True
while running:

    SCREEN.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -player_speed
            if event.key == pygame.K_RIGHT:
                player_x_change = player_speed
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Player movement
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= SCREEN_WIDTH - 64:
        player_x = SCREEN_WIDTH - 64

    # Enemy movement
    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 1
        enemy_y += enemy_y_change
    elif enemy_x >= SCREEN_WIDTH - 64:
        enemy_x_change = -1
        enemy_y += enemy_y_change

    # Bullet movement
    if bullet_y <= 0:
        bullet_y = player_y
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # Collision
    collision = is_collision(enemy_x, enemy_y, bullet_x, bullet_y)
    if collision:
        bullet_y = player_y
        bullet_state = "ready"
        score += 1
        enemy_x = random.randint(0, SCREEN_WIDTH - 64)
        enemy_y = random.randint(50, 150)

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    show_score()

    pygame.display.update()

pygame.quit()
print("Final Score:", score)
