import pygame
import sys
import clicker
import generator
import button
import random
import time
import company

# program loop Boolean
in_program = True

# while program running
while in_program:

    pygame.init()   # initialize pygame

    # set up the application window
    size = width, height = 400, 600     # set the screen size
    screen = pygame.display.set_mode(size)  # create the screen
    pygame.display.set_caption("Pollution Clicker") # set the window caption
    icon = pygame.image.load("earth.png")   # prepare the window icon
    pygame.display.set_icon(icon)           # set the window icon

    # set up sounds
    pygame.mixer.music.load("Pollution.wav")        # load music
    pygame.mixer.music.play(-1)                     # play music on loop
    pygame.mixer.music.set_volume(0.2)              # set music volume
    click_sound = pygame.mixer.Sound("click.mp3")   # load clicking sound

    # set up the clicker
    group = pygame.sprite.RenderPlain()     # create a sprite group
    my_clicker = clicker.Clicker(screen)    # create the clicker
    group.add(my_clicker)                   # add the clicker to the sprite group

    # initialize important game variables
    pollution = 1000    # measures pollution (win lose conditions)
    money = 0           # measures money for buying generators

    background = pygame.image.load("background.png")    # set up image for background

    font = pygame.font.Font(None, 20)   # set up font

    # set up sprites for counting generators
    volunteer_count = pygame.sprite.Sprite()        # for counting volunteers
    volunteer_group_count = pygame.sprite.Sprite()  # for counting volunteer groups
    recycle_plant_count = pygame.sprite.Sprite()    # for counting recycle plants
    gift_shop_count = pygame.sprite.Sprite()        # for counting gift shops
    donation_count = pygame.sprite.Sprite()         # for counting donators
    grant_count = pygame.sprite.Sprite()            # for counting grants
    factory_count = pygame.sprite.Sprite()          # for counting factories
    factory_count_2 = pygame.sprite.Sprite()        # for extra text explaining factories

    # store generator info
    generators = {"volunteer": 0, "volunteer group": 0, "recycle plant": 0, \
                  "gift shop": 0, "donator": 0, "grant": 0, "factory": 0}       # store counts of generators
    generator_list = [] # store generators

    # set up buttons
    buttons = pygame.sprite.RenderPlain()   # create sprite group for buttons
    v_button = button.Button("Volunteer: $50, -1 pollution/sec", 50, 1, -1)             # create volunteer button
    v_g_button = button.Button("Volunteer Group: $200, -5 pollution/sec", 200, 1, -5)   # create volunteer group button
    r_p_button = button.Button("Recycle Plant: $1000, -50 pollution/sec", 1000, 1, -50) # create recycle plant button
    g_s_button = button.Button("Open gift shop: $10, +$1/sec", 10, 1, 0, 1)             # create gift shop button
    d_button = button.Button("Earn donations: $100, +$15/sec", 100, 1, 0, 15)           # create donator button
    g_button = button.Button("Apply for grant: $500, $100/sec", 500, 1, 0, 100)         # create grant button
    v_button.rect.right = screen.get_rect().right - 2   # set right border of volunteer button
    v_g_button.rect.right = screen.get_rect().right - 2 # set right border of volunteer group button
    r_p_button.rect.right = screen.get_rect().right - 2 # set right border of recycle plant button
    g_s_button.rect.right = screen.get_rect().right - 2 # set right border of gift shop button
    d_button.rect.right = screen.get_rect().right - 2   # set right border of donator button
    g_button.rect.right = screen.get_rect().right - 2   # set right border of grant button
    v_button.rect.top = 2                               # set top of volunteer button
    v_g_button.rect.top = 18                            # set top of volunteer group button
    r_p_button.rect.top = 34                            # set top of recycle plant button
    g_s_button.rect.top = 66                            # set top of gift shop button
    d_button.rect.top = 82                              # set top of donator button
    g_button.rect.top = 98                              # set top of grant button
    buttons.add(v_button)   # add volunteer button to sprite group
    buttons.add(v_g_button) # add volunteer group button to sprite group
    buttons.add(r_p_button) # add recycle plant button to sprite group
    buttons.add(g_s_button) # add gift shop button to sprite group
    buttons.add(d_button)   # add donator button to sprite group
    buttons.add(g_button)   # add grant button to sprite group

    # set up companies
    companies = pygame.sprite.RenderPlain() # create sprite group for companies

    # create a generator for passivly generating pollution
    passive = generator.Generator(1, 1) # create generator
    generator_list.append(passive)      # add generator to list

    # set up Booleans for creating factories
    first_factory = False   # for checking if factory 1 exists
    second_factory = False  # for checking if factory 2 exists
    third_factory = False   # for checking if factory 3 exists
    fourth_factory = False  # for checking if factory 4 exists

    # game loop Booleans
    lose = False    # for game loop after loss
    win = False     # for game loop after win
    running = True  # for main game loop
    setup = True    # for tutorial game loop

    # set up text lines for tutorial
    lines = []                                  # initialize as list
    line_group = pygame.sprite.RenderPlain()    # create sprite group for text line sprites
    # add sprites to list and sprite group
    for i in range(22):
        lines.append(pygame.sprite.Sprite(line_group))  # create sprite and add it to list and sprite group

    # begin tutorial game loop
    while setup:

        # event handling
        for event in pygame.event.get():

            # if program end, game loop Booleans to False
            if event.type == pygame.QUIT:
                setup = False       # tutorial game loop Boolean to False
                running = False     # main game loop Boolean to False
                in_program = False  # program running loop Boolean to False

            # if mouse click, end tutorial game loop
            if event.type == pygame.MOUSEBUTTONUP:
                setup = False   # tutorial game loop Boolean to False

        # create images with tutorial text
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
        # create images 11-20 as empty
        for i in range(11, 21):
            lines[i].image = font.render("", True, (0,0,0))
        lines[21].image = font.render("sound effects from ZapSplat.com", True, (100,100,100))   # text for sources

        # get rects for each text line
        y = 200     # start at y 200
        # get rect from each text line
        for i in range(22):
            lines[i].rect = lines[i].image.get_rect()               # get rect from text line
            lines[i].rect.center = (screen.get_rect().center[0], y) # move rect
            y += 16                                                 # change y so next text rect is lower

        # display on screen
        screen.fill((255, 255, 255))    # fill screen with white
        line_group.draw(screen)         # draw text lines on screen
        pygame.display.update()         # update screen

    # set up timers
    start_time = time.time()    # timer for passive pollution
    factory_start = time.time() # timer for company creation
    hint_time = time.time()     # timer for managing hints

    hint_mode = 0   # used for managing hints

    # begin main game loop
    while running == True:

        # add the background image to the screen
        screen.blit(background, (0, 0))

        # handle passive pollution
        # if enough time has passed, double passive polution
        if int(time.time()) - int(start_time) >= 15:
            passive.pol = passive.pol * 2   # double passive polution
            start_time = time.time()        # reset timer

            # if passive pollution is to high, lower it
            if passive.pol >= 700:
                passive.pol = 700   # lower passive polution

        # event handling
        for event in pygame.event.get():

            # if program end, set game loop Booleans to False
            if event.type == pygame.QUIT:
                running = False     # main game loop Boolean to False
                in_program = False  # program running Boolean to False

            # if mouse click, check if it clicked on a hitbox
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()    # get mouse position

                # if clicked on clicker, change polution and money
                if my_clicker.rect.collidepoint(pos):
                    result = my_clicker.click() # run click method on clicker
                    pollution += result[0]      # modify pollution
                    money += result[1]          # modify money
                    click_sound.play()          # play clicker sound

                # handle clicked buttons
                clicked_buttons = [b for b in buttons if b.rect.collidepoint(pos)]  # get clicked buttons
                # click buttons
                for b in clicked_buttons:
                    result = b.click(money) # click button
                    money += result[0]      # spend money

                    # if generator was created, add it
                    if isinstance(result[1], generator.Generator):
                        generator_list.append(result[1])    # add generator to list

                        # figure out which generator was created and count it
                        if b.pollution_modifier == -1:          # generator is volunteer
                            generators["volunteer"] += 1        # count volunteer
                        elif b.pollution_modifier == -5:        # generator is volunteer group
                            generators["volunteer group"] += 1  # count volunteer group
                        elif b.pollution_modifier == -50:       # generator is recycle plant
                            generators["recycle plant"] += 1    # count recycle plant
                        elif b.pollution_modifier == 10:        # generator is factory
                            generators["factory"] += 1          # count factory
                        elif b.money == 1:                      # generator is gift shop
                            generators["gift shop"] += 1        # count gift shop
                        elif b.money == 15:                     # generator is donator
                            generators["donator"] += 1          # count donator
                        elif b.money == 100:                    # generator is grant
                            generators["grant"] += 1            # count grant

                # handle companies that were clicked
                clicked_companies = [c for c in companies if c.rect.collidepoint(pos)]  # get clicked companies
                # click companies
                for c in clicked_companies:
                    c.click()   # click company

        # Define when each company will start attempting to create factories
        factory_end = time.time()                           # End factory timer
        factory_time = int(factory_end) - int(factory_start)# Calculate amount of time passed
        
        if factory_time >= 40 and not(first_factory):       # After 40 seconds, create the first company once
            companies.add(company.Company(2, 456))          # Define location of the company icon
            first_factory = True                            # Set flag true to prevent repeating first factory
            
        if factory_time >= 80 and not(second_factory):      # After 80 seconds, create the second company once
            companies.add(company.Company(102, 456))        # Define location of the company icon
            second_factory = True                           # Set flag true to prevent repeats
            
        if factory_time >= 120 and not(third_factory):      # After 120 seconds, create the third company once
            companies.add(company.Company(202, 456))        # Define location of company icon
            third_factory = True                            # Set flag true to prevent repeats
            
        if factory_time >= 160 and not(fourth_factory):     # After 160 seconds, create the fourth company once
            companies.add(company.Company(302, 456))        # Define location of company icon
            fourth_factory = True                           # Set flag true to prevent repeats

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

        

        #display generator counters
        list_items = 0  # start amount of generator counts displayed at 0
        # if at least 1 gift shop, create its counter text
        if generators["gift shop"] > 0:
            gift_shop_count.image = font.render("Gift Shops: " + str(generators["gift shop"]), True, (0,0,0))   # make image for text
            gift_shop_count.rect = pygame.Rect(0, list_items*16 + 2, 1, 1)                                      # get image location
            list_items += 1                                                                                     # mark as being displayed
            group.add(gift_shop_count)                                                                          # prepare to be drawn to screen
        else:
            group.remove(gift_shop_count)
        # if at least 1 donator, create its counter text
        if generators["donator"] > 0:
            donation_count.image = font.render("Donators: " + str(generators["donator"]), True, (0,0,0))
            donation_count.rect = pygame.Rect(0, list_items*16 + 2, 1, 1)
            list_items += 1
            group.add(donation_count)
        else:
            group.remove(donation_count)
        # if at least 1 grant, create its counter text
        if generators["grant"] > 0:
            grant_count.image = font.render("Grants earned: " + str(generators["grant"]), True, (0,0,0))
            grant_count.rect = pygame.Rect(0, list_items*16 + 2, 1, 1)
            list_items += 1
            group.add(grant_count)
        else:
            group.remove(grant_count)
        # if at least 1 volunteer, create its counter text
        if generators["volunteer"] > 0:
            volunteer_count.image = font.render("Volunteers: " + str(generators["volunteer"]), True, (0,0,0))
            volunteer_count.rect = pygame.Rect(0, list_items*16 + 2, 1, 1)
            list_items += 1
            group.add(volunteer_count)
        else:
            group.remove(volunteer_count)
        # if at least 1 volunteer group, create its counter text
        if generators["volunteer group"] > 0:
            volunteer_group_count.image = font.render("Volunteer Groups: " + str(generators["volunteer group"]), True, (0,0,0))
            volunteer_group_count.rect = pygame.Rect(0, list_items*16 + 2, 1, 1)
            list_items += 1
            group.add(volunteer_group_count)
        else:
            group.remove(volunteer_group_count)
        # if at least 1 recycle plant, create its counter text
        if generators["recycle plant"] > 0:
            recycle_plant_count.image = font.render("Recycle Plants: " + str(generators["recycle plant"]), True, (0,0,0))
            recycle_plant_count.rect = pygame.Rect(0, list_items*16 + 2, 1, 1)
            list_items += 1
            group.add(recycle_plant_count)
        else:
            group.remove(recycle_plant_count)
        # if at least 1 factory, create its counter text
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

        # get image for counters
        passive_text = font.render("Passive Pollution: +" + str(passive.pol) + "/sec", True, (0,0,0))   # for passive pollution counter
        pollution_text = font.render("Pollution: " + str(pollution), True, (0,0,0))                     # for pollution counter
        money_text = font.render("$" + str(money), True, (0,0, 0))                                      # for money counter

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
