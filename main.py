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
my_clicker = clicker.Clicker(screen)
group.add(my_clicker)

pollution = 1000
money = 0

font = pygame.font.Font(None, 16)

volunteer_count = pygame.sprite.Sprite()
volunteer_group_count = pygame.sprite.Sprite()
recycle_plant_count = pygame.sprite.Sprite()
factory_count = pygame.sprite.Sprite()

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
companies = pygame.sprite.RenderPlain()

companies.add(company.Company(2, 547))

start_time = time.time()

while True:

    screen.fill((0, 191, 255))

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


            clicked_companies = [c for c in companies if c.rect.collidepoint(pos)]

            for c in clicked_companies:
                c.click()
            


    for comp in companies:
        result = comp.tick()
        if isinstance(result, generator.Generator):
            generators["factory"] += 1
            generator_list.append(result)
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(comp.rect.left, comp.rect.bottom + 1, comp.get_progress()*comp.rect.width, 10))
        

    for gen in generator_list:
        result = gen.add()
        pollution += result[0]
        money += result[1]

    
    pollution_text = font.render("Pollution: " + str(pollution), True, (0,0,0))
    pollution_text_rect = pygame.Rect(0,400, 100, 100)
    money_text = font.render("$" + str(money), True, (0,0,0))
    money_text_rect = pygame.Rect(0, 500, 100, 100)


    list_items = 0
    if generators["volunteer"] > 0:
        volunteer_count.image = font.render("Volunteers (-1 pollution/sec): " + str(generators["volunteer"]), True, (0,0,0))
        volunteer_count.rect = pygame.Rect(0, list_items*16, 1, 1)
        list_items += 1
        group.add(volunteer_count)
    else:
        group.remove(volunteer_count)
    if generators["volunteer group"] > 0:
        volunteer_group_count.image = font.render("Volunteer Groups: " + str(generators["volunteer group"]), True, (0,0,0))
        volunteer_group_count.rect = pygame.Rect(0, list_items*16, 1, 1)
        list_items += 1
        group.add(volunteer_group_count)
    else:
        group.remove(volunteer_group_count)
    if generators["recycle plant"] > 0:
        recycle_plant_count.image = font.render("Recycle Plants: " + str(generators["recycle plant"]), True, (0,0,0))
        recycle_plant_count.rect = pygame.Rect(0, list_items*16, 1, 1)
        list_items += 1
        group.add(recycle_plant_count)
    else:
        group.remove(recycle_plant_count)
    if generators["factory"] > 0:
        factory_count.image = font.render("Factories: " + str(generators["factory"]), True, (0,0,0))
        factory_count.rect = pygame.Rect(0, list_items*16, 1, 1)
        list_items += 1
        group.add(factory_count)
    else:
        group.remove(factory_count)
    
    
    screen.blit(pollution_text, (0, 400))
    screen.blit(money_text, (0, 500))

    companies.draw(screen)
    buttons.draw(screen)
    group.draw(screen)
    pygame.display.update()
