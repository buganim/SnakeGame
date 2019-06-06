import numpy as np
from colorama import Back


class Board:

    def __init__(self,game):
        self.score = 0
        self.snake = game.snake
        self.apple = game.apple
        self.height = game.size
        self.width = game.size
        self.matrix = np.matrix([[0] * self.height] * self.width)
        while self.snake.place == self.apple.place:
            self.apple.reroll()

    def updateBoard(self):
        if self.snake.place == self.apple.place:
            self.apple.reroll()
            self.score += 1
            self.snake.grow()

        self.clearBoard()
        for cord in self.snake.trail:
            y = cord[0]
            x = cord[1]
            self.matrix[y,x] = 1
        self.matrix[self.apple.placementY,self.apple.placementX] = 2

    def clearBoard(self):
        for row in range(self.height):
            for cell in range(self.width):
                self.matrix[row,cell] = 0
    
    def __str__(self):
        str_matrix = ""
        return_matrix = ""
        for one in self.matrix:
            str_matrix += "{}\n".format(one)
        for one in str_matrix:
            if one == '[' or one == ']':
                continue
            if one == "0":
                return_matrix += Back.WHITE + " "
                continue
            if one == "1":
                return_matrix += Back.GREEN + " "
                continue
            if one == "2":
                return_matrix += Back.RED + " "
                continue
            else:
                return_matrix += one
        return(return_matrix)