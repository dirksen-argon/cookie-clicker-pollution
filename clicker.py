if __name__ != "__main__":
    
    import pygame

    # class for the "clicker" of a clicker game
    # changes stats when clicked
    class Clicker(pygame.sprite.Sprite):

        # constructor
        def __init__(self, screen):
            
            super().__init__()                                          # parent class constructor
            self.image = pygame.image.load("earth.png")                 # get image of earth to represent clicker
            self.image = pygame.transform.scale(self.image, (200, 200)) # scale image to fit in 200x200 area
            self.rect = self.image.get_rect()                           # get hitbox of image
            self.rect.center = screen.get_rect().center                 # move hitbox (and image) to center of screen

        # runs on click
        def click(self):

            # return change in pollution and change in money
            return -1, 1
        
else:
    print("99 bottles")
