from tkinter import *

from point import Point


class Field(object):
    def __init__(self, master, n, cell_size, press_callback=None):
        self.canvas = Canvas(master, width=(n + 2) * cell_size, height=(n + 2) * cell_size,
                             bg='red')
        self.canvas.focus_set()
        self.canvas.pack()

        self.points = []
        # start draw
        self.sharp = [] # canv obj



    def choosed_point(self) -> Point:
        pass

