import pygame
import math

# Initialize Pygame
pygame.init()

# Display setup
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("waveTek")

clock = pygame.time.Clock()
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)

# Line setup
numLines = 100
spacing = 6
amplitude = 150     # maximum vertical displacement
speed = 0.03        # speed of wave motion

# Create lines: each has an x-position and phase offset
lines = []
for i in range(numLines):
    x = 50 + i * spacing
    phase = i * 0.05     # phase offset (radians)
    lines.append((x, phase))

# Game loop
running = True
time = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time += speed  # increment time to drive sine wave

    # Draw everything
    WINDOW.fill(WHITE)
    for x, phase in lines:
        # Compute smooth sinusoidal offset
        offset = math.sin(time + phase) * amplitude

        yCenter = HEIGHT // 2
        yTop = yCenter - 100 + offset
        yBottom = yCenter + 100 + offset

        pygame.draw.line(WINDOW, BLUE, (x, yTop), (x, yBottom), 1)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
