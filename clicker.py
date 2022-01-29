if __name__ != "__main__":
    import pygame

    class Clicker(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.money = 0
            self.image = pygame.image.load("dollar.png")
            self.rect = pygame.Rect((0,0), (100,200))
            self.rect.center = (50, 100)
        def click(self):
            self.money = self.money + 1
            return -1
        #heya
else:
    print("99 bottles")
