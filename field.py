from tkinter import *

from point import Point


class Field(object):
    def __init__(self, master, n, press_callback=None):
        self.canvas = Canvas(master, width=800, height=800, bg='red')
        self.points = []
        # start draw
        self.sharp = [] # canv obj
        
        self.canvas.focus_set()
        self.canvas.pack()

    def choosed_point(self) -> Point:
        pass

