from tkinter import *

from point import Point
from config import *

import math


def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class Field(Canvas):
    def __init__(self, master, press_callback=None):
        n = Config.Field.CELL_COUNT
        l = Config.Field.CELL_SIZE
        size = (n + 1) * l
        super().__init__(master, width=size, height=size,
                        bg='gray', highlightthickness=0)
        self.focus_set()
        self.create_rectangle(1, 1, size - 1, size - 1, fill=Config.Field.CANV_COLOR, width=2)
        # draw the lines
        for i in range(n + 1):
            self.create_line(l * i, 0, l * i, size)
            self.create_line(0, l * i, size, l * i)
        self.points = [[None] * n for i in range(n)]

        for i in range(n):
            for j in range(n):
                self.points[i][j] = Point(self, l * (i + 1), l * (j + 1), 2, Config.Point.UNUSED_COLOR)
                self.points[i][j].draw()
        # todo: new handle cover points
        self.covered_point = None
        self.bind('<Motion>', lambda e: self.cover_handle(e.x, e.y))
        def press(event):
            i, j = self.nearest_point(event.x, event.y)
            if i != -1:
                press_callback(i, j)
        self.bind('<Button-1>', press)

    def cover_handle(self, x, y):
        if self.covered_point is not None:
            self.covered_point.uncover()
        i, j = self.nearest_point(x, y)
        self.covered_point = self.points[i][j] if i != -1 else None
        if self.covered_point is not None:
            self.covered_point.cover()

    def nearest_point(self, x, y):
        for i in range(len(self.points)):
            for j in range(len(self.points[i])):
                point = self.points[i][j]
                if dist(x, y, point.x, point.y) < Config.Field.VICINITY_DIST:
                    return (i, j)
        return (-1, -1)

    def update(self, info):
        pass
