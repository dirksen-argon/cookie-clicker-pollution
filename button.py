if __name__ != "__main__":

    import pygame
    import generator
    import clicker
    
    class Button(pygame.sprite.Sprite):

        def __init__(self, text, cost, pollution_modifier, time):
            super().__init__()
            font = pygame.font.Font(None, 16)
            self.image = font.render(text)
            self.rect = self.image.get_rect()
            self.pollution_modifier = pollution_modifier
            self.cost = cost
            self.time = time

        def click(self, money):
            if cost >= money:
                return -cost, generator.Generator()
