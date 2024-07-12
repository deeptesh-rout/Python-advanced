import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Traffic vs. Zombie Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Player
player_size = 50
player_pos = [SCREEN_WIDTH//2, SCREEN_HEIGHT-2*player_size]

# Enemy
enemy_size = 50
enemy_pos = [random.randint(0, SCREEN_WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]

# Zombie
zombie_size = 50
zombie_pos = [random.randint(0, SCREEN_WIDTH-zombie_size), 0]
zombie_list = [zombie_pos]

# Speed
SPEED = 10
ZOMBIE_SPEED = 5

# Score
score = 0
font = pygame.font.SysFont("monospace", 35)

# Functions
def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, SCREEN_WIDTH-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(SCREEN, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < SCREEN_HEIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1
    return score

def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False

def drop_zombies(zombie_list):
    delay = random.random()
    if len(zombie_list) < 5 and delay < 0.1:
        x_pos = random.randint(0, SCREEN_WIDTH-zombie_size)
        y_pos = 0
        zombie_list.append([x_pos, y_pos])

def draw_zombies(zombie_list):
    for zombie_pos in zombie_list:
        pygame.draw.rect(SCREEN, RED, (zombie_pos[0], zombie_pos[1], zombie_size, zombie_size))

def update_zombie_positions(zombie_list, score):
    for idx, zombie_pos in enumerate(zombie_list):
        if zombie_pos[1] >= 0 and zombie_pos[1] < SCREEN_HEIGHT:
            zombie_pos[1] += ZOMBIE_SPEED
        else:
            zombie_list.pop(idx)
            score += 1
    return score

def collision_check_zombies(zombie_list, player_pos):
    for zombie_pos in zombie_list:
        if detect_collision(zombie_pos, player_pos):
            return True
    return False

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

# Game loop
game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 10
    if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - player_size:
        player_pos[0] += 10

    SCREEN.fill(WHITE)

    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)
    if collision_check(enemy_list, player_pos):
        game_over = True
        break

    draw_enemies(enemy_list)

    drop_zombies(zombie_list)
    score = update_zombie_positions(zombie_list, score)
    if collision_check_zombies(zombie_list, player_pos):
        game_over = True
        break

    draw_zombies(zombie_list)

    pygame.draw.rect(SCREEN, BLACK, (player_pos[0], player_pos[1], player_size, player_size))

    text = "Score: " + str(score)
    label = font.render(text, 1, BLACK)
    SCREEN.blit(label, (SCREEN_WIDTH-200, SCREEN_HEIGHT-40))

    clock.tick(30)
    pygame.display.update()

print("Final Score: ", score)
