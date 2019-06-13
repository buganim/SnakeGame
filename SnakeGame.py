from pynput.keyboard import Key, Listener
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


class SnakeGame:

    def __init__(self, size):
        self.size = size
        self.snake = Snake(self)
        self.apple = Apple(self)
        self.board = Board(self)
        self.board.updateBoard()
        self.keyListener = Listener(on_press=self.on_press)
        self.isGameRunning = True

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
        self.isGameRunning = False
        return ("Game Ended, Score: {} !!!".format(self.board.score))

    def on_press(self, key):
        key = key.char

        if key == 'a' or key == 's' or key == 'w' or key == 'd':
            self.snake.setLastDirection(key)

    def __str__(self):
        return ("Board:\n{}".format(self.board.__str__()) + Style.RESET_ALL + "\n Score: {}\n".format(self.board.score))


@d.timeit
def play(boardSize, difficulty):
    game = SnakeGame(boardSize)
    print(game.__str__())

    def moveAlone():

        ts = time.time()
        while game.isGameRunning:
            te = time.time()
            if te - ts > difficulty:
                if not game.makeMove(game.snake.lastDirection):
                    break
                ts = time.time()

    t1 = Thread(target=moveAlone)
    t1.start()
    game.keyListener.start()
    t1.join()
    game.keyListener.join()


if __name__ == '__main__':
    print("Game Time: " + play(10, 0.5))
