from tkinter import *

from start_menu import StartMenu
from game_menu import GameMenu
from field import Field
from config import *


class GameInterface(Tk):
    def __init__(self, choose_point_callback):
        super().__init__()
        self.locked = False
        n = Config.Field.CELL_COUNT
        l = Config.Field.CELL_SIZE
        hsize = (n + 1) * l + 2 * Config.Field.CANV_INDENTS
        self.withdraw()
        self.start_menu = StartMenu(self)
        self.title('POP-Go')
        root_size = ((Config.Field.CELL_COUNT + 1) * l + Config.GameMenu.SIZE + 3 * Config.Field.CANV_INDENTS)
        self.geometry('{}x{}'.format(root_size, hsize))
        self.resizable(height=False, width=False)
        self.field = Field(self, choose_point_callback)
        self.field.place(x=Config.Field.CANV_INDENTS, y=Config.Field.CANV_INDENTS)

        self.game_menu = GameMenu(self)
        self.game_menu.place(x=2 * Config.Field.CANV_INDENTS + (n + 1) * l, y=Config.Field.CANV_INDENTS)

    def change(self, hull, score1, score2, points):
        self.field.draw_hull(hull, points)
        self.game_menu.score(score1, score2)

    def lock(self):
        self.locked = True
        self.field.lock()

    def unlock(self):
        self.locked = False
        self.field.unlock()
