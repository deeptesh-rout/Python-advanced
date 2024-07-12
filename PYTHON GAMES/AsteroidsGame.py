import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids Game")

# Set up colors
WHITE = (255, 255, 255)

# Set up the player
player_img = pygame.image.load('ship.png').convert_alpha()
player_img = pygame.transform.scale(player_img, (50, 50))
player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
player_angle = 0
player_speed = 5

# Set up bullets
bullet_img = pygame.Surface((5, 5))
bullet_img.fill(WHITE)
bullets = []

# Set up asteroids
asteroids = []
num_asteroids = 5
for _ in range(num_asteroids):
    asteroid_img = pygame.Surface((30, 30))
    pygame.draw.circle(asteroid_img, WHITE, (15, 15), 15)
    asteroid_rect = asteroid_img.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
    asteroids.append(asteroid_rect)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_angle += 5
    if keys[pygame.K_RIGHT]:
        player_angle -= 5
    if keys[pygame.K_UP]:
        dx = math.cos(math.radians(player_angle)) * player_speed
        dy = -math.sin(math.radians(player_angle)) * player_speed
        player_rect.move_ip(dx, dy)
    if keys[pygame.K_SPACE]:
        bullet_rect = bullet_img.get_rect(center=player_rect.center)
        bullet_rect.angle = player_angle
        bullets.append(bullet_rect)
    
    # Bullet movement
    for bullet in bullets:
        dx = math.cos(math.radians(bullet.angle)) * 10
        dy = -math.sin(math.radians(bullet.angle)) * 10
        bullet.move_ip(dx, dy)
    
    # Asteroid movement
    for asteroid in asteroids:
        asteroid.x += random.randint(-2, 2)
        asteroid.y += random.randint(-2, 2)
    
    # Drawing
    rotated_player_img = pygame.transform.rotate(player_img, player_angle)
    player_rect = rotated_player_img.get_rect(center=player_rect.center)
    screen.blit(rotated_player_img, player_rect)
    
    for bullet in bullets:
        screen.blit(bullet_img, bullet)
    
    for asteroid in asteroids:
        screen.blit(asteroid_img, asteroid)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
