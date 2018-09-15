from tkinter import *

from point import Point
from start_menu import StartMenu
from field import Field
from game_menu import GameMenu
from config import Config

root = Tk()
root.withdraw()
sm = StartMenu(root)
root.title("POP-GO")
root_size = (Config.Field.CELL_COUNT + 1) * Config.Field.CELL_SIZE + 20
root.geometry('{}x{}'.format(root_size, root_size))
root.resizable(height=False, width=False)


field = Field(root, lambda i, j: print(i, j))
field.place(x=Config.Field.CANV_INDENTS, y=Config.Field.CANV_INDENTS)
root.mainloop()


