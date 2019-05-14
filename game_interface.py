from tkinter import *

from start_menu import StartMenu
from game_menu import GameMenu
from field import Field
from config import *


class GameInterface(Tk):
    def __init__(self, choose_point_callback, concede_callback=None):
        super().__init__()
        self.config(bg=Config.GUI.COLOR)
        #self.withdraw()
        #self.start_menu = StartMenu(self)

        n = Config.Field.CELL_COUNT
        l = Config.Field.CELL_SIZE
        canvas_size = (n + 1) * l + 2 * Config.Field.CANV_INDENTS
        self.title('POP-Go')
        root_size = ((Config.Field.CELL_COUNT + 1) * l + Config.GameMenu.SIZE + 3 * Config.Field.CANV_INDENTS)
        self.geometry('{}x{}'.format(root_size, canvas_size))
        self.resizable(height=False, width=False)

        self.locked = False

        self.field = Field(self, choose_point_callback)
        self.field.place(x=Config.Field.CANV_INDENTS, y=Config.Field.CANV_INDENTS)

        self.game_menu = GameMenu(self)
        self.game_menu.place(x=2 * Config.Field.CANV_INDENTS + (n + 1) * l, y=Config.Field.CANV_INDENTS)

    def display(self, hull, score1, score2, points):
        self.field.display(hull, points)
        self.game_menu.score(score1, score2)

    def lock(self):
        self.locked = True
        self.field.lock()
        self.game_menu.lock()

    def unlock(self):
        self.locked = False
        self.field.unlock()
        self.game_menu.unlock()

    def report(self, s):
        self.start_menu.report(s)
