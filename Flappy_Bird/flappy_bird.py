import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
PIPE_WIDTH, PIPE_HEIGHT = 50, random.randint(50, 250)
BIRD_WIDTH, BIRD_HEIGHT = 40, 40
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Game Variables
bird_x, bird_y = WIDTH // 4, HEIGHT // 2
bird_vel = 0
gravity = 1
jump = -10
pipes = [{"x": WIDTH, "y": 0, "height": PIPE_HEIGHT}]
score = 0

# Game Loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_vel = jump

    # Update bird's position
    bird_vel += gravity
    bird_y += bird_vel

    # Update pipe positions
    for pipe in pipes:
        pipe["x"] -= 5
        if pipe["x"] < -PIPE_WIDTH:
            pipes.remove(pipe)
            pipes.append({"x": WIDTH, "y": 0, "height": random.randint(50, 250)})
        if bird_x + BIRD_WIDTH > pipe["x"] and bird_x < pipe["x"] + PIPE_WIDTH:
            if bird_y < pipe["height"] or bird_y + BIRD_HEIGHT > pipe["height"] + 150:
                running = False
        if pipe["x"] == bird_x:
            score += 1

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (bird_x, bird_y, BIRD_WIDTH, BIRD_HEIGHT))
    for pipe in pipes:
        pygame.draw.rect(screen, WHITE, (pipe["x"], pipe["y"], PIPE_WIDTH, pipe["height"]))
        pygame.draw.rect(screen, WHITE, (pipe["x"], pipe["height"] + 150, PIPE_WIDTH, HEIGHT - pipe["height"] - 150))
    pygame.display.flip()

    clock.tick(FPS)

# Quit Pygame
pygame.quit()
