import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Egg Catcher Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (165, 42, 42)

# Clock
clock = pygame.time.Clock()

# Basket
basket_width = 100
basket_height = 50
basket_pos = [SCREEN_WIDTH//2, SCREEN_HEIGHT - basket_height - 10]
basket_speed = 20

# Egg
egg_width = 30
egg_height = 40
egg_pos = [random.randint(0, SCREEN_WIDTH - egg_width), 0]
egg_speed = 10
egg_list = [egg_pos]

# Score
score = 0
font = pygame.font.SysFont("monospace", 35)

# Functions
def drop_eggs(egg_list):
    delay = random.random()
    if len(egg_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, SCREEN_WIDTH - egg_width)
        y_pos = 0
        egg_list.append([x_pos, y_pos])

def draw_eggs(egg_list):
    for egg_pos in egg_list:
        pygame.draw.ellipse(SCREEN, BROWN, (egg_pos[0], egg_pos[1], egg_width, egg_height))

def update_egg_positions(egg_list, score):
    for idx, egg_pos in enumerate(egg_list):
        if egg_pos[1] >= 0 and egg_pos[1] < SCREEN_HEIGHT:
            egg_pos[1] += egg_speed
        else:
            egg_list.pop(idx)
            score -= 1
    return score

def collision_check(egg_list, basket_pos):
    for egg_pos in egg_list:
        if detect_collision(egg_pos, basket_pos):
            egg_list.remove(egg_pos)
            return True
    return False

def detect_collision(egg_pos, basket_pos):
    e_x = egg_pos[0]
    e_y = egg_pos[1]

    b_x = basket_pos[0]
    b_y = basket_pos[1]

    if (e_x >= b_x and e_x < (b_x + basket_width)) or (b_x >= e_x and b_x < (e_x + egg_width)):
        if (e_y >= b_y and e_y < (b_y + basket_height)) or (b_y >= e_y and b_y < (e_y + egg_height)):
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

    if keys[pygame.K_LEFT] and basket_pos[0] > 0:
        basket_pos[0] -= basket_speed
    if keys[pygame.K_RIGHT] and basket_pos[0] < SCREEN_WIDTH - basket_width:
        basket_pos[0] += basket_speed

    SCREEN.fill(WHITE)

    drop_eggs(egg_list)
    score = update_egg_positions(egg_list, score)
    if collision_check(egg_list, basket_pos):
        score += 1

    draw_eggs(egg_list)

    pygame.draw.rect(SCREEN, BLUE, (basket_pos[0], basket_pos[1], basket_width, basket_height))

    text = "Score: " + str(score)
    label = font.render(text, 1, BLACK)
    SCREEN.blit(label, (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 40))

    clock.tick(30)
    pygame.display.update()

print("Final Score: ", score)
