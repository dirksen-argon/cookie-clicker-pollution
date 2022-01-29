if __name__ != "__main__":
    import pygame
    import time

    class Generator:
        def __init__(self):
            start = time.time()
        def add(self):
            end = time.time()
            house = int(end) - int(start)
            if house >= 1:
                start = time.time()
                return 1
            else:
                return 0
else:
    print(" of pop ")
