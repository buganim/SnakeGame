import numpy as np


class Snake:

    def __init__(self, game):
        self.size = game.size
        self.length = 0
        self.placementX = int(self.size/2)
        self.placementY = int(self.size/2)
        self.place = [self.placementY, self.placementX]
        self.lastLoaction = self.place
        self.trail = [[self.placementY, self.placementX]]
        self.lastDirection = "w"

    def move(self, direction):
        self.updateLastLocation()

        if direction == "w":  # UP
            if(self.placementY == 0):
                return False
            self.placementY = self.placementY - 1
            self.lastDirection = "w"

        if direction == "s":  # DOWN
            if(self.placementY == self.size-1):
                return False
            self.placementY = self.placementY + 1
            self.lastDirection = "s"

        if direction == "a":  # LEFT
            if(self.placementX == 0):
                return False
            self.placementX = self.placementX - 1
            self.lastDirection = "a"

        if direction == "d":  # RIGHT
            if(self.placementX == self.size-1):
                return False
            self.placementX = self.placementX + 1
            self.lastDirection = "d"

        self.updateLocation()
        if self.place in self.trail:
            return False

        self.trail.insert(0, [self.placementY, self.placementX])
        try:
            self.trail.pop(self.length+1)
        except:
            pass

        return True

    def updateLocation(self):
        self.place = [self.placementY, self.placementX]

    def updateLastLocation(self):
        self.lastLoaction = [self.placementY, self.placementX]

    def grow(self):
        self.length += 1

    def __str__(self):
        return (self.placementY, self.placementX)
