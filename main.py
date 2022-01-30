import pygame
import sys
import clicker
import generator
import button
import random
import time
import company

in_program = True
while in_program:
    pygame.init()

    size = width, height = 400, 600

    screen = pygame.display.set_mode(size)

    pygame.mixer.music.load("Pollution.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    group = pygame.sprite.RenderPlain()
    my_clicker = clicker.Clicker(screen)
    group.add(my_clicker)

    pollution = 1000
    money = 0

    background = pygame.image.load("background.png")

    click_sound = pygame.mixer.Sound("click.mp3")

    font = pygame.font.Font(None, 20)

    volunteer_count = pygame.sprite.Sprite()
    volunteer_group_count = pygame.sprite.Sprite()
    recycle_plant_count = pygame.sprite.Sprite()
    gift_shop_count = pygame.sprite.Sprite()
    donation_count = pygame.sprite.Sprite()
    grant_count = pygame.sprite.Sprite()
    factory_count = pygame.sprite.Sprite()
    factory_count_2 = pygame.sprite.Sprite()

    generators = {"volunteer": 0, "volunteer group": 0, "recycle plant": 0, \
                  "gift shop": 0, "donator": 0, "grant": 0, "factory": 0}

    buttons = pygame.sprite.RenderPlain()

    v_button = button.Button("Volunteer: $50, -1 pollution/sec", 50, 1, -1)
    v_g_button = button.Button("Volunteer Group: $200, -5 pollution/sec", 200, 1, -5)
    r_p_button = button.Button("Recycle Plant: $1000, -50 pollution/sec", 1000, 1, -50)
    g_s_button = button.Button("Open gift shop: $10, +$1/sec", 10, 1, 0, 1)
    d_button = button.Button("Earn donations: $100, +$15/sec", 100, 1, 0, 15)
    g_button = button.Button("Apply for grant: $500, $100/sec", 500, 1, 0, 100)


    v_button.rect.right = screen.get_rect().right - 2
    v_g_button.rect.right = screen.get_rect().right - 2
    r_p_button.rect.right = screen.get_rect().right - 2
    g_s_button.rect.right = screen.get_rect().right - 2
    d_button.rect.right = screen.get_rect().right - 2
    g_button.rect.right = screen.get_rect().right - 2
    v_button.rect.top = 2
    v_g_button.rect.top = 18
    r_p_button.rect.top = 34
    g_s_button.rect.top = 66
    d_button.rect.top = 82
    g_button.rect.top = 98

    buttons.add(v_button)
    buttons.add(v_g_button)
    buttons.add(r_p_button)
    buttons.add(g_s_button)
    buttons.add(d_button)
    buttons.add(g_button)

    generator_list = []
    companies = pygame.sprite.RenderPlain()

    passive = generator.Generator(1, 1)
    generator_list.append(passive)



    first_factory = False
    second_factory = False
    third_factory = False
    fourth_factory = False
    lose = False
    win = False
    running = True


    setup = True
    lines = []
    line_group = pygame.sprite.RenderPlain()
    for i in range(22):
        lines.append(pygame.sprite.Sprite(line_group))

    while setup:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                setup = False
                running = False
                in_program = False
            if event.type == pygame.MOUSEBUTTONUP:
                setup = False

        screen.fill((255, 255, 255))


        lines[0].image = font.render("Pollution is a major problem today, and is only", True, (0,0,0))
        lines[1].image = font.render("set to get worse as time goes on. Save the world", True, (0,0,0))
        lines[2].image = font.render("by reducing pollution.", True, (0,0,0))
        lines[3].image = font.render("", True, (0,0,0))
        lines[4].image = font.render("Click on the Earth to earn money and reduce pollution.", True, (0,0,0))
        lines[5].image = font.render("Spend money on ways to reduce pollution. Careful,", True, (0,0,0))
        lines[6].image = font.render("the rate of pollution is rising. Stop companies from", True, (0,0,0))
        lines[7].image = font.render("building pollution generating factories. Get to 0", True, (0,0,0))
        lines[8].image = font.render("pollution to win. You lose if it reaches 10,000.", True, (0,0,0))
        lines[9].image = font.render("", True, (0,0,0))
        lines[10].image = font.render("Click anywhere to start", True, (0,0,0))
        for i in range(11, 21):
            lines[i].image = font.render("", True, (0,0,0))
        lines[21].image = font.render("sound effects from ZapSplat.com", True, (100,100,100))
        y = 200
        for i in range(22):
            lines[i].rect = lines[i].image.get_rect()
            lines[i].rect.center = (screen.get_rect().center[0], y)
            y += 16

        line_group.draw(screen)
        pygame.display.update()

    start_time = time.time()
    factory_start = time.time()
    hint_time = time.time()
    hint_mode = 0

    while running == True:

        screen.blit(background, (0, 0))


        if int(time.time()) - int(start_time) >= 15:
            passive.pol = passive.pol * 2
            start_time = time.time()
            if passive.pol >= 700:
                passive.pol = 700

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                in_program = False
                
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if my_clicker.rect.collidepoint(pos):
                    result = my_clicker.click()
                    pollution += result[0]
                    money += result[1]
                    click_sound.play()

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

        factory_end = time.time()
        factory_time = int(factory_end) - int(factory_start)
        if factory_time >= 40 and not(first_factory):
            companies.add(company.Company(2, 456))
            first_factory = True
        if factory_time >= 80 and not(second_factory):
            companies.add(company.Company(102, 456))
            second_factory = True
        if factory_time >= 120 and not(third_factory):
            companies.add(company.Company(202, 456))
            third_factory = True
        if factory_time >= 160 and not(fourth_factory):
            companies.add(company.Company(302, 456))
            fourth_factory = True

        if pollution >= 10000:
            lose = True
            break

        if pollution <= 0:
            win = True
            break

        for comp in companies:
            result = comp.tick()
            if isinstance(result, generator.Generator):
                generators["factory"] += 1
                generator_list.append(result)
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(comp.rect.left, comp.rect.bottom + 1, comp.get_progress()*comp.rect.width, 10))
            
        your_hand = False
        position = pygame.mouse.get_pos()
        if my_clicker.rect.collidepoint(position):
            your_hand = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        for be in buttons:
            if be.rect.collidepoint(position):
                your_hand = True
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        for pol in companies:
            if pol.rect.collidepoint(position):
                your_hand = True
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        if your_hand == False:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for gen in generator_list:
            result = gen.add()
            pollution += result[0]
            money += result[1]


        passive_text = font.render("Passive Pollution: +" + str(passive.pol) + "/sec", True, (0,0,0))    
        pollution_text = font.render("Pollution: " + str(pollution), True, (0,0,0))
        money_text = font.render("$" + str(money), True, (0,0, 0))


        list_items = 0
        if generators["gift shop"] > 0:
            gift_shop_count.image = font.render("Gift Shops: " + str(generators["gift shop"]), True, (0,0,0))
            gift_shop_count.rect = pygame.Rect(0, list_items*16 + 2, 1, 1)
            list_items += 1
            group.add(gift_shop_count)
        else:
            group.remove(gift_shop_count)
        if generators["donator"] > 0:
            donation_count.image = font.render("Donators: " + str(generators["donator"]), True, (0,0,0))
            donation_count.rect = pygame.Rect(0, list_items*16 + 2, 1, 1)
            list_items += 1
            group.add(donation_count)
        else:
            group.remove(donation_count)
        if generators["grant"] > 0:
            grant_count.image = font.render("Grants earned: " + str(generators["grant"]), True, (0,0,0))
            grant_count.rect = pygame.Rect(0, list_items*16 + 2, 1, 1)
            list_items += 1
            group.add(grant_count)
        else:
            group.remove(grant_count)
        if generators["volunteer"] > 0:
            volunteer_count.image = font.render("Volunteers: " + str(generators["volunteer"]), True, (0,0,0))
            volunteer_count.rect = pygame.Rect(0, list_items*16 + 2, 1, 1)
            list_items += 1
            group.add(volunteer_count)
        else:
            group.remove(volunteer_count)
        if generators["volunteer group"] > 0:
            volunteer_group_count.image = font.render("Volunteer Groups: " + str(generators["volunteer group"]), True, (0,0,0))
            volunteer_group_count.rect = pygame.Rect(0, list_items*16 + 2, 1, 1)
            list_items += 1
            group.add(volunteer_group_count)
        else:
            group.remove(volunteer_group_count)
        if generators["recycle plant"] > 0:
            recycle_plant_count.image = font.render("Recycle Plants: " + str(generators["recycle plant"]), True, (0,0,0))
            recycle_plant_count.rect = pygame.Rect(0, list_items*16 + 2, 1, 1)
            list_items += 1
            group.add(recycle_plant_count)
        else:
            group.remove(recycle_plant_count)
        if generators["factory"] > 0:
            factory_count.image = font.render("Factories: " + str(generators["factory"]), True, (0,0,0))
            factory_count.rect = pygame.Rect(0, list_items*16 + 2, 1, 1)
            factory_count_2.image = font.render("    (+100 pollution/sec)", True, (0,0,0))
            factory_count_2.rect = pygame.Rect(0, (list_items + 1)*16 + 2, 1, 1)
            list_items += 2
            group.add(factory_count)
            group.add(factory_count_2)
        else:
            group.remove(factory_count)
            group.remove(factory_count_2)

        passive_text_rect = passive_text.get_rect()
        pollution_text_rect = pollution_text.get_rect()
        money_text_rect = pollution_text.get_rect()
        passive_text_rect.right = screen.get_rect().right - 2
        pollution_text_rect.right = screen.get_rect().right - 2
        money_text_rect.right = screen.get_rect().right - 2
        passive_text_rect.top = 130
        pollution_text_rect.top = 162
        money_text_rect.top = 178

        screen.blit(passive_text, passive_text_rect)
        screen.blit(pollution_text, pollution_text_rect)
        screen.blit(money_text, money_text_rect)

        if time.time() - hint_time <= 0.1:
            hint_color = (255, 255, 255)
        else:
            hint_color = (0,0,0)
            
        bottom_text = pygame.sprite.Sprite(group)
        bottom_text.image = pygame.Surface((screen.get_rect().width, 36))
        bottom_text.rect = bottom_text.image.get_rect()
        bottom_text.rect.topleft = (0, screen.get_rect().bottom - 36)
        bottom_text.image.fill(hint_color)

        

        companies.draw(screen)
        buttons.draw(screen)
        group.draw(screen)

        
        
        if pollution >= 5000:
            if hint_mode != 4:
                hint_time = time.time()
                hint_mode = 4
            text_1 = font.render("Hint: If you reach 10,000 pollution, you lose", True, (255, 255, 255))
            text_2 = font.render("", True, (255, 255, 255))
        elif first_factory:
            if hint_mode != 3:
                hint_time = time.time()
                hint_mode = 3
            text_1 = font.render("Hint: Click on the company to prevent it from", True, (255,255,255))
            text_2 = font.render("building harmful factories", True, (255, 255, 255))
        elif passive.pol > 1:
            if hint_mode != 2:
                hint_time = time.time()
                hint_mode = 2
            text_1 = font.render("Hint: The passive pollution rate will rise over time", True, (255, 255, 255))
            text_2 = font.render("", True, (255, 255, 255))
        elif money >= 10:
            if hint_mode != 1:
                hint_time = time.time()
                hint_mode = 1
            text_1 = font.render("Hint: You can spend money using the buttons in the top right", True, (255, 255, 255))
            text_2 = font.render("", True, (255, 255, 255))
        else:
            hint_mode = 0
            text_1 = font.render("Hint: Click the Earth to reduce pollution and earn money", True, (255, 255, 255))
            text_2 = font.render("", True, (255, 255, 255))
            
        screen.blit(text_1, (bottom_text.rect.x + 1, bottom_text.rect.y + 1))
        screen.blit(text_2, (bottom_text.rect.x + 1, bottom_text.rect.y + 17))
        pygame.display.update()

    # Get the start time for the click buffer
    buffer_start = time.time()

    # If the player has lost, run this loop
    while lose == True:

        # Get end time for buffer and calculate number of seconds since loop's beginning
        buffer_end = time.time()
        buffer = int(buffer_end) - int(buffer_start)

        # Set the mouse to an arrow if it wasn't one already
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # Make the background white
        screen.fill((255, 255, 255))

        # Create and display lose text
        big_font = pygame.font.Font(None, 55)                   # Create the font
        image = big_font.render("Game Over!", True, (0, 0, 0))  # Create the text
        text = image.get_rect()                                 # Create hitbox of the text
        text.center = screen.get_rect().center                  # Move text to location
        screen.blit(image, text)                                # Display on screen

        # Create and display top text
        image = font.render("If nothing is done soon, the", \   # Create the text (font already created)
                            True, (0, 0, 0))
        text = image.get_rect()                                 # Create hitbox of the text
        text.center = (200, 490)                                # Move text to location
        screen.blit(image, text)                                # Display on screen

        # Create and display bottom text
        image = font.render("effects of pollution will be out of control", \# Create the text (font already created)
                            True, (0, 0, 0))
        text = image.get_rect()                                             # Create hitbox of the text
        text.center = (200, 510)                                            # Move text to location
        screen.blit(image, text)                                            # Display on screen

        # Create and display loop option
        image = font.render("click to try again", True, (0, 0, 0))  # Create the text (font already created)
        text = image.get_rect()                                     # Create hitbox of the text
        text.center = (200, 570)                                    # Move text to location
        screen.blit(image, text)                                    # Display on screen

        # Display all text and backgrounds to the pygame window
        pygame.display.flip()

        # Checking pygame for user input
        for event in pygame.event.get():
            # If the player quits, quit the program
            if event.type == pygame.QUIT:
                lose = False
                in_program = False
            # If the player clicks, restart the game
            elif event.type == pygame.MOUSEBUTTONUP and buffer >= 2:
                lose = False

    # if the player has won, run this loop            
    while win == True:

        # Get end time for buffer and calculate number of seconds since loop's beginning
        buffer_end = time.time()
        buffer = int(buffer_end) - int(buffer_start)

        # Set the mouse to an arrow if it wasn't one already
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # Make the background green
        screen.fill((0, 255, 127))

        # Create and display win text
        big_font = pygame.font.Font(None, 55)                       # Create the font
        image = big_font.render("You Won!", True, (42, 79, 138))    # Create the text
        text = image.get_rect()                                     # Create hitbox of the text
        text.center = screen.get_rect().center                      # Move text to location
        screen.blit(image, text)                                    # Display on screen

        # Create and display top text
        image = font.render("If we act fast, we can reverse the", \ # Create the text (font already created)
                            True, (42, 79, 138))
        text = image.get_rect()                                     # Create hitbox of the text
        text.center = (200, 490)                                    # Move text to location
        screen.blit(image, text)                                    # Display on screen

        # Create and display bottom text
        image = font.render("effects of pollution across the globe", \  # Create the text (font already created)
                            True, (42, 79, 138))
        text = image.get_rect()                                         # Create hitbox of the text
        text.center = (200, 510)                                        # Move text to location
        screen.blit(image, text)                                        # Display on screen

        # Create and display loop option
        image = font.render("click to play again", True, (42, 79, 138)) # Create the text (font already created)
        text = image.get_rect()                                         # Create hitbox of the text
        text.center = (200, 570)                                        # Move text to location
        screen.blit(image, text)                                        # Display on screen

        # Display all text and backgrounds to the pygame window
        pygame.display.flip()

        # Checking pygame for user input
        for event in pygame.event.get():
            # If the player quits, quit the program
            if event.type == pygame.QUIT:
                win = False
                in_program = False
            # If the player clicks, restart the game
            elif event.type == pygame.MOUSEBUTTONUP and buffer >= 2:
                win = False

    # Close the pygame window, restarts game if click and closes if quit
    pygame.quit()
