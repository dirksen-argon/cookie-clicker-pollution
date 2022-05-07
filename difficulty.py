if __name__ != "__main__":

    import pygame

    class Difficulty(pygame.sprite.Sprite): # Create Difficulty Class

        def __init__(self, text, sound):

            super().__init__()
            self.text = text
            font = pygame.font.Font(None, 60)
            self.image = pygame.Surface(font.render(text, True, (0,0,0)).get_rect().size)
            self.rect = self.image.get_rect()
            self.image.fill((255,255,255))
            self.image.blit(font.render(text, True, (0,0,0)), self.rect)
            self.sound = sound

        def click(self):

            return self.text
            sound.play()
