if __name__ != "__main__":

    import pygame
    import generator
    import clicker

    # class for buttons that spend money and create generators
    class Button(pygame.sprite.Sprite):

        # constructor
        def __init__(self, text, cost, time, pollution_modifier=0, money=0):

            super().__init__()                                      # parent class constructor
            font = pygame.font.Font(None, 20)                       # get font for button text
            self.text = font.render(text, True, (0,0,0))            # create image with button text
            self.image = pygame.Surface(self.text.get_rect().size)  # set image for button
            self.rect = self.image.get_rect()                       # set hitbox of button
            pygame.draw.rect(self.image, (56, 245, 85), self.rect)  # draw the background on the image
            self.image.blit(self.text, self.rect)                   # put the text on the button image
            self.pollution_modifier = pollution_modifier            # store the pollution modifier (how much generators made by this button affect pollution by)
            self.cost = cost                                        # store the cost of pushing this button
            self.time = time                                        # store the time for generators made by this button to tick
            self.money = money                                      # store the money generators mad by this button generate
            self.sound = pygame.mixer.Sound("purchase.mp3")         # store the sound made when a sucessful purchase is made

        # runs when button is clicked
        # return a tuple containing how much money is spent and a generator (if applicable)
        def click(self, money):

            # if user has enough money, create a generator
            if self.cost <= money:
                self.sound.play()                                                                       # play the purchase sound
                return -self.cost, generator.Generator(self.time, self.pollution_modifier, self.money)  # return the cost and new generator

            # no money is spent and no generator is created if user does not have enough money
            else:
                return 0, None
