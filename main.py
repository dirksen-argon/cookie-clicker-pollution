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
gift_shop_count = pygame.sprite.Sprite()
donation_count = pygame.sprite.Sprite()
grant_count = pygame.sprite.Sprite()
factory_count = pygame.sprite.Sprite()

generators = {"volunteer": 0, "volunteer group": 0, "recycle plant": 0, \
              "gift shop": 0, "donator": 0, "grant": 0, "factory": 0}

buttons = pygame.sprite.RenderPlain()
v_button = button.Button("Volunteer: $50, -1 pollution/sec", 50, 1, -1)
v_g_button = button.Button("Volunteer Group: $200, -5 pollution/sec", 200, 1, -5)
r_p_button = button.Button("Recycle Plant: $1000, -50 pollution/sec", 1000, 1, -50)
g_s_button = button.Button("Open gift shop: $10, +$1/sec", 10, 1, 0, 1)
d_button = button.Button("Earn donations: $100, +$15/sec", 100, 1, 0, 15)
g_button = button.Button("Apply for grant: $500, $100/sec", 500, 1, 0, 100)


v_button.rect.right = screen.get_rect().right
v_g_button.rect.right = screen.get_rect().right
r_p_button.rect.right = screen.get_rect().right
g_s_button.rect.right = screen.get_rect().right
d_button.rect.right = screen.get_rect().right
g_button.rect.right = screen.get_rect().right
v_button.rect.top = 0
v_g_button.rect.top = 16
r_p_button.rect.top = 32
g_s_button.rect.top = 48
d_button.rect.top = 64
g_button.rect.top = 80


buttons.add(v_button)
buttons.add(v_g_button)
buttons.add(r_p_button)
buttons.add(g_s_button)
buttons.add(d_button)
buttons.add(g_button)

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
                    elif b.money == 1:
                        generators["gift shop"] += 1
                    elif b.money == 15:
                        generators["donator"] += 1
                    elif b.money == 100:
                        generators["grant"] += 1


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
    if generators["gift shop"] > 0:
        gift_shop_count.image = font.render("Gift Shops: " + str(generators["gift shop"]), True, (0,0,0))
        gift_shop_count.rect = pygame.Rect(0, list_items*16, 1, 1)
        list_items += 1
        group.add(gift_shop_count)
    else:
        group.remove(gift_shop_count)
    if generators["donator"] > 0:
        donation_count.image = font.render("Donators: " + str(generators["donator"]), True, (0,0,0))
        donation_count.rect = pygame.Rect(0, list_items*16, 1, 1)
        list_items += 1
        group.add(donation_count)
    else:
        group.remove(donation_count)
    if generators["grant"] > 0:
        grant_count.image = font.render("Grants earned: " + str(generators["grant"]), True, (0,0,0))
        grant_count.rect = pygame.Rect(0, list_items*16, 1, 1)
        list_items += 1
        group.add(grant_count)
    else:
        group.remove(grant_count)
    if generators["volunteer"] > 0:
        volunteer_count.image = font.render("Volunteers: " + str(generators["volunteer"]), True, (0,0,0))
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
