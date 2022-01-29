import pygame
import sys
import clicker

pygame.init()

size = width, height = 400, 600

screen = pygame.display.set_mode(size)

group = pygame.sprite.RenderPlain()
my_clicker = clicker.Clicker()
group.add(my_clicker)

pollution = 0
money = 0

font = pygame.font.Font(None, 16)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if my_clicker.rect.collidepoint(pos):
                result = my_clicker.click()
                pollution += result[0]
                money += result[1]

            

    screen.fill((0, 191, 255))
    pollution_text = font.render("Pollution: " + str(pollution), True, (0,0,0))
    pollution_text_rect = pygame.Rect(0,400, 100, 100)
    money_text = font.render("$" + str(money), True, (0,0,0))
    money_text_rect = pygame.Rect(0, 500, 100, 100)
    
    screen.blit(pollution_text, (0, 400))
    screen.blit(money_text, (0, 500))
    
    group.draw(screen)
    pygame.display.update()
