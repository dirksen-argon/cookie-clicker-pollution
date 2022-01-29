if __name__ != __main__:
    import pygame

    class Clicker(pygame.Sprite):
        def __init__(self):
            super().__init__()
            self.money = 0
            self.image = pygame.image.load("dollar.png")
            self.rect = self.image.get_rect()
            self.rect.center = (100, 200)
        def click(self):
            self.money = self.money + 1
            return -1
else:
    print("99 bottles")
