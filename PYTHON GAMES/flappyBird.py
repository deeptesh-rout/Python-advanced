import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
BACKGROUND_COLOR = (0, 0, 0)
BIRD_COLOR = (255, 255, 0)
PIPE_COLOR = (0, 255, 0)
GRAVITY = 0.25
FLAP_STRENGTH = 6
GAP_HEIGHT = 200
PIPE_WIDTH = 70
PIPE_SPEED = 3

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0
        self.image = pygame.Surface((20, 20))
        self.image.fill(BIRD_COLOR)

    def flap(self):
        self.velocity = -FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50, HEIGHT - GAP_HEIGHT - 50)

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self):
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, 0, PIPE_WIDTH, self.height))
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, self.height + GAP_HEIGHT, PIPE_WIDTH, HEIGHT))

# Main function
def main():
    bird = Bird()
    pipes = []
    frame_count = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        screen.fill(BACKGROUND_COLOR)

        if frame_count % 100 == 0:
            pipes.append(Pipe(WIDTH))

        for pipe in pipes:
            pipe.update()
            pipe.draw()

            if pipe.x < -PIPE_WIDTH:
                pipes.remove(pipe)

            if bird.x < pipe.x + PIPE_WIDTH and bird.x + 20 > pipe.x:
                if bird.y < pipe.height or bird.y + 20 > pipe.height + GAP_HEIGHT:
                    running = False

        bird.update()
        bird.draw()

        if bird.y > HEIGHT or bird.y < 0:
            running = False

        pygame.display.update()
        frame_count += 1

        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
