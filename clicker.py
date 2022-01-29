if __name__ != "__main__":
    import pygame

    class Clicker(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("earth.png")
            self.image = pygame.transform.scale(self.image, (200, 200))
            self.rect = self.image.get_rect()
            self.rect.center = (50, 100)
        def click(self):
            return -1, 1
else:
    print("99 bottles")
