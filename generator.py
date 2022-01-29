if __name__ != "__main__":
    import pygame
    import time

    class Generator:
        def __init__(self, num, pol = 0, money = 0):
            self.start = time.time()
            self.pol = pol
            self.num = num
            self.money = money
        def add(self):
            end = time.time()
            house = int(end) - int(self.start)
            if house >= self.num:
                self.start = time.time()
                return self.pol, self.money
            else:
                return (0, 0)
else:
    print(" of pop ")
