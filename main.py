import pygame
import sys
import clicker
import generator
import button
import random
import time
import company

pygame.init()

size = width, height = 400, 600

screen = pygame.display.set_mode(size)

group = pygame.sprite.RenderPlain()
my_clicker = clicker.Clicker()
group.add(my_clicker)

pollution = 1000
money = 0

font = pygame.font.Font(None, 16)

volunteer_count = pygame.sprite.Sprite(group)
volunteer_group_count = pygame.sprite.Sprite(group)
recycle_plant_count = pygame.sprite.Sprite(group)
factory_count = pygame.sprite.Sprite(group)

generators = {"volunteer": 0, "volunteer group": 0, "recycle plant": 0, \
              "factory": 0}

buttons = pygame.sprite.RenderPlain()
v_button = button.Button("Volunteer $50 -1 pollution/sec", 50, -1, 1)
v_g_button = button.Button("Volunteer Group $200 -5 pollution/sec", 200, -5, 1)
r_p_button = button.Button("Recycle Plant $1000 -50 pollution/sec", 1000, -50, 1)

v_button.rect.x = 200
v_g_button.rect.x = 200
r_p_button.rect.x = 200
v_button.rect.y = 300
v_g_button.rect.y = 350
r_p_button.rect.y = 400

buttons.add(v_button)
buttons.add(v_g_button)
buttons.add(r_p_button)

generator_list = []
companies = []

start_time = time.time()

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

            clicked_buttons = [b for b in buttons if b.rect.collidepoint(pos)]

            for b in clicked_buttons:
                result = b.click(money)
                money += result[0]
                if isinstance(result[1], generator.Generator):
                    generator_list.append(result[1])
                    if b.pollution_modifier == -1:
                        generators["volunteer"] += 1
                    elif b.pollution_modifier == -5:
                        generators["volunteer group"] += 1
                    elif b.pollution_modifier == -50:
                        generators["recycle plant"] += 1
                    elif b.pollution_modifier == 10:
                        generators["factory"] += 1
            

    if int(time.time()) - int(start_time) >= 5:
        start_time = time.time()
        new_company = company.Company()
        companies.append(new_company)

    for comp in companies:
        result = comp.tick()
        if isinstance(result, generator.Generator):
            generators["factory"] += 1
            generator_list.append(result)
        

    for gen in generator_list:
        result = gen.add()
        pollution += result[0]
        money += result[1]

    screen.fill((0, 191, 255))
    pollution_text = font.render("Pollution: " + str(pollution), True, (0,0,0))
    pollution_text_rect = pygame.Rect(0,400, 100, 100)
    money_text = font.render("$" + str(money), True, (0,0,0))
    money_text_rect = pygame.Rect(0, 500, 100, 100)

    volunteer_count.image = font.render("Volunteers: " + str(generators["volunteer"]), None, (0,0,0))
    volunteer_count.rect = pygame.Rect(200, 0, 1, 1)
    volunteer_group_count.image = font.render("Volunteer Groups: " + str(generators["volunteer group"]), None, (0,0,0))
    volunteer_group_count.rect = pygame.Rect(200, 50, 1, 1)
    recycle_plant_count.image = font.render("Recycle Plants: " + str(generators["recycle plant"]), None, (0,0,0))
    recycle_plant_count.rect = pygame.Rect(200, 100, 1, 1)
    factory_count.image = font.render("Factories: " + str(generators["factory"]), None, (0,0,0))
    factory_count.rect = pygame.Rect(200, 150, 1, 1)
    
    
    screen.blit(pollution_text, (0, 400))
    screen.blit(money_text, (0, 500))

    buttons.draw(screen)
    group.draw(screen)
    pygame.display.update()
