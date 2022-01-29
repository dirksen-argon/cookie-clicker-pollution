import pygame
import sys
import clicker

pygame.init()

size = width, height = 400, 600

screen = pygame.display.set_mode(size)

group = pygame.sprite.RenderPlain()
group.add(clicker.Clicker())


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((100,100,100))
    group.draw(screen)
    pygame.display.update()
