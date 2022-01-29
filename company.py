if __name__ != "__main__":
    import pygame
    import time
    import generator

    class Company(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.start = time.time()
            self.image = pygame.image.load("factory.png")
            self.image = pygame.transform.scale(self.image, (40, 40))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
        def tick(self):
            end = time.time()
            house = int(end) - int(self.start)
            if house >= 3:
                self.start = time.time()
                factory = generator.Generator(1)
                return factory
            else:
                return None
        def get_progress(self):
            end = time.time()
            house = (end - self.start)/3
            return house
else:
    print("on the wall")
