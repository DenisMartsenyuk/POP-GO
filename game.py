from inside import Logic
from game_interface import GameInterface

from config import *


class Game(object):
    def __init__(self):
        self.logic = Logic(Config.Field.CELL_COUNT)

        # call after making turn
        def choose_callback(i, j):
            #self.game_interface.lock(): for mulitplayer
            self.ans = self.logic.do_turn(i, j)
            self.game_interface.display(self.ans, self.logic.count1, self.logic.count2, self.logic.table)

        self.game_interface = GameInterface(choose_callback)
        self.game_interface.mainloop()

if __name__ == '__main__':
    Game()
