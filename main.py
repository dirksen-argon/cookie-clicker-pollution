import pygame
import sys

pygame.init()

size = width, height = 400, 600

screen = pygame.display.set_mode(size)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
