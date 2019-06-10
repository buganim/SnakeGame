import os
import sys
import time
from Board import Board
from Snake import Snake
from Apple import Apple
from colorama import init
from colorama import Style
import decorators as d
from threading import Thread

init()
ts = time.time()


class SnakeGame:

    def __init__(self, size):
        self.size = size
        self.snake = Snake(self)
        self.apple = Apple(self)
        self.board = Board(self)
        self.board.updateBoard()

    def makeMove(self, move):
        if self.snake.move(move):
            self.board.updateBoard()
            os.system('cls')
            print(self.__str__())
        else:
            print(self.endGame())
            return False
        return True

    def endGame(self):
        return ("Game Ended, Score: {} !!!".format(self.board.score))

    def __str__(self):
        return ("Board:\n{}".format(self.board.__str__()) + Style.RESET_ALL + "\n Score: {}\n".format(self.board.score))

@d.timeit
def play(boardSize,difficulty):
    game = SnakeGame(boardSize)
    print(game.__str__())


    def moveAlone():
        global ts
        while True:
            te = time.time()
            if te - ts > difficulty:
                if not game.makeMove(game.snake.lastDirection):
                    break
                ts = time.time()

    def movePlayer():
        global ts
        while t1.isAlive():
            ts = time.time()
            next_move = input()
            if not next_move == 'a' and not next_move == 's' and not next_move == 'w' and not next_move == 'd':
                ts = time.time()
                continue
            if not game.makeMove(next_move):
                break

    t2 = Thread(target=movePlayer)
    t1 = Thread(target=moveAlone)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    print("Game Time: " + play(10,0.5))
