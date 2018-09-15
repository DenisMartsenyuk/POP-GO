from tkinter import *

from point import Point
from start_menu import StartMenu
from field import Field
from game_menu import GameMenu
from config import Config
from game_menu import GameMenu

n = Config.Field.CELL_COUNT
l = Config.Field.CELL_SIZE
hsize = (n + 1) * l + 2 * Config.Field.CANV_INDENTS

root = Tk()
root.withdraw()
sm = StartMenu(root)
root.title("POP-GO")
root_size = ((Config.Field.CELL_COUNT + 1) * l + Config.GameMenu.SIZE + 3 * Config.Field.CANV_INDENTS)
root.geometry('{}x{}'.format(root_size, hsize))
root.resizable(height=False, width=False)


field = Field(root, lambda i, j: print(i, j))
field.place(x=Config.Field.CANV_INDENTS, y=Config.Field.CANV_INDENTS)

game_menu = GameMenu(root)
game_menu.place(x=2 * Config.Field.CANV_INDENTS + (n + 1) * l, y=Config.Field.CANV_INDENTS)

root.mainloop()


