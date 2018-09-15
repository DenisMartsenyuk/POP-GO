from tkinter import *

from point import Point
from config import *

class Field(object):
    def __init__(self, master, press_callback=None):
        l = Config.Field.CELL_SIZE
        lb = Config.Field.LINE_BD
        rb = Config.Field.RECT_BD
        n = Config.Field.CELL_COUNT
        ci = Config.Field.CANV_INDENTS
        rw = l * (n + 1) + l * lb + 2 * rb
        size = rw + 2 * ci
        self.canvas = Canvas(master, width=size, height=size,
                             bg='gray', highlightthickness=0)
        #self.canvas.create_rectangle()
        self.canvas.focus_set()
        self.canvas.pack()
        x1 = y1 = ci
        x2 = y2 = ci + rw
        self.canvas.create_rectangle(x1, y1, x2, y2, fill='red')
        self.points = []
        # start draw
        self.sharp = [] # canv obj



    def choosed_point(self) -> Point:
        pass

