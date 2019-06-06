import random


class Apple:

    def __init__(self, game):
        self.snake = game.snake
        self.size = game.size
        self.placementX = random.randint(0, self.size-1)
        self.placementY = random.randint(0, self.size-1)
        self.place = [self.placementY, self.placementX]
        self.lastPlace = self.place

    def reroll(self):
        self.placementX = random.randint(0, self.size-1)
        self.placementY = random.randint(0, self.size-1)
        self.place = [self.placementY, self.placementX]
        while self.place in self.snake.trail:
            self.reroll()

    def __str__(self):
        return (self.placementY, self.placementX)
