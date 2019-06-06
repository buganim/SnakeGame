import os
import sys
import time
# import curses
from Board import Board
from Snake import Snake
from Apple import Apple
from colorama import init
from colorama import Style

init()


class SnakeGame:

    def __init__(self, size):
        self.size = size
        self.snake = Snake(self)
        self.apple = Apple(self)
        self.board = Board(self)
        self.board.updateBoard()

    def endGame(self):
        return("Game Ended, Score: {} !!!".format(self.board.score))

    def __str__(self):
        return("Board:\n{}".format(self.board.__str__()) + Style.RESET_ALL + "\n Snake: {}\n Apple: {}\n Score: {}\n SnakeLength: {}\n".format(self.snake.__str__(), self.apple.__str__(), self.board.score, self.snake.length))


if __name__ == '__main__':
    # stdscr = curses.initscr()
    # curses.noecho()
    # curses.cbreak()
    game = SnakeGame(5)
    print(game.__str__())

    while True:
        next_move = input()
        if not next_move == 'a' and not next_move == 's' and not next_move == 'w' and not next_move == 'd':
            continue

        if game.snake.move(next_move):
            game.board.updateBoard()
            time.sleep(0.1)
            os.system('cls')
            # print(game.__str__())
            # stdscr.addstr(game.__str__())
            # stdscr.refresh()
        else:
            print(game.endGame())
            break
