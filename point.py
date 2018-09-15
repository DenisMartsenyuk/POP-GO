from tkinter import *

from config import *

class Point(object):
    def __init__(self, canvas: Canvas, x, y, r, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.instance = None

    def draw(self):
        self.instance = self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                                fill=self.color, outline=self.color)

    def hide(self):
        self.canvas.delete(self.instance)
        self.instance = None

    def update(self):
        self.hide()
        self.draw()

    def cover(self):
        self.r = Config.Point.COVER_RADIUS
        self.update()

    def uncover(self):
        self.r = Config.Point.RADIUS
        self.update()
