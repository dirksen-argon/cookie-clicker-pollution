if __name__ != "__main__":
    import pygame
    import time
    import generator
    import random

    class Company:
        location = ((50, 50), (50, 100), (100, 100), (50, 150), (50, 200), \
                    (50, 250), (50, 300), (50, 350))
        def __init__(self):
            start = time.time()
            self.image = pygame.image.load("factory.png")
            self.image = pygame.transform.scale(self.image, (40, 40))
            self.rect = self.image.get_rect()
            self.rect.center = random.choice(location)
        def click(self):
            end = time.time()
            house = int(end) - int(start)
            if house >= 3:
                start = time.time()
                factory = generator.Generator()
                return factory
            else:
                return None
else:
    print("on the wall")
