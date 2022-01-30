if __name__ != "__main__":
    
    import pygame
    import time
    import generator

    # class for companies that will create factory generators if left unchecked
    # when clicked, companies are slowed down in creating factories
    class Company(pygame.sprite.Sprite):

        # constructor
        def __init__(self, x, y):
            
            super().__init__()                                          # parent constructor
            self.start = time.time()                                    # save time of creation
            self.image = pygame.image.load("factory.png")               # set image of company
            self.image = pygame.transform.scale(self.image, (94, 94))   # resize image
            self.rect = self.image.get_rect()                           # get hitbox
            self.sound = pygame.mixer.Sound("factory_built.mp3")        # set factory creation sound
            self.rect.topleft = (x, y)                                  # set location of image

        # runs once per tick
        def tick(self):
            
            end = time.time()                   # get current time
            house = int(end) - int(self.start)  # get time since last set time

            # if 10+ seconds have passed, create a factory
            if house >= 10:
                self.start = time.time()                # reset clock to now
                factory = generator.Generator(1, 100)   # create new generator
                self.sound.play()                       # play factory creation sound
                return factory                          # return the new factory

            # if 10+ seconds haven't passed, do nothing
            else:
                return None

        # return decimal (0-1) representing how close to building a factory the company is
        def get_progress(self):
            
            end = time.time()               # get current time
            house = (end - self.start)/10   # get decimal representing how close to factory creation
            return house                    # return the decimal

        # runs when Company is clicked
        def click(self):
            
            end = time.time()   # get the current time

            # if moving the timer start 2 seconds forward doesn't move it past now, do it
            if self.start + 2 <= end:
                self.start = self.start + 2     # move the timer start 2 seconds later

            # reset the timer start
            else:
                self.start = end    # reset the timer start
                
else:
    print("on the wall")
