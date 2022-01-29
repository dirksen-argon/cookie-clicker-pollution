if __name__ != "__main__":

    import pygame
    import generator
    import clicker
    
    class Button(pygame.sprite.Sprite):

        def __init__(self, text, cost, time, pollution_modifier=0, money=0):
            super().__init__()
            font = pygame.font.Font(None, 16)
            self.image = font.render(text, True, (0,0,0))
            self.rect = self.image.get_rect()
            self.pollution_modifier = pollution_modifier
            self.cost = cost
            self.time = time
            self.money = money

        def click(self, money):
            if self.cost <= money:
                return -self.cost, generator.Generator(self.time, self.pollution_modifier, self.money)
            else:
                return 0, None
