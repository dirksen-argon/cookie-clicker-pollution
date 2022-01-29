if __name__ != "__main__":
    import pygame
    import time

    class Generator:
        def __init__(self, num, pol):
            start = time.time()
            self.pol = pol
            self.num = num
        def add(self):
            end = time.time()
            house = int(end) - int(start)
            if house >= self.num:
                start = time.time()
                return self.pol
            else:
                return 0
else:
    print(" of pop ")
