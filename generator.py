if __name__ != "__main__":
    
    import pygame
    import time

    # class for modifying pollution and money over time
    class Generator:

        # constructor
        def __init__(self, num, pol = 0, money = 0):
            
            self.start = time.time()    # start a timer
            self.pol = pol              # store the effect on pollution
            self.num = num              # store how long it takes to make a change
            self.money = money          # store the effect on money

        # runs once per tick
        def add(self):

            # return pollution and money change
            
            end = time.time()                   # get current time
            house = int(end) - int(self.start)  # compare current time to timer start

            # if enough time has passed to tick, make changes to pollution and money
            if house >= self.num:
                self.start = time.time()    # reset timer
                return self.pol, self.money # return changes to pollution and money

            # no change to pollution or money
            else:
                return (0, 0)
            
else:
    print(" of pop ")
