from tkinter import *

from point import Point
from config import *

import math


def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

color = {-1: Config.Point.PLAYER2_COLOR, 0: Config.Point.UNUSED_COLOR, 1: Config.Point.PLAYER1_COLOR}

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
        for j in range(n):
            for i in range(n):
                self.points[i][j] = Point(self, l * (i + 1), l * (j + 1), Config.Point.RADIUS, Config.Point.UNUSED_COLOR)
                self.points[i][j].draw()
        self.covered_point = None
        self.bind('<Motion>', lambda e: self.cover_handle(e.x, e.y))
        def press(event):
            point = self.nearest_active_point(event.x, event.y)
            if point is not None:
                press_callback(point.y // Config.Field.CELL_SIZE - 1, point.x // Config.Field.CELL_SIZE - 1)
        self.bind('<Button-1>', press)
        self.hulls = []

    def cover_handle(self, x, y):
        if self.covered_point is not None:
            self.covered_point.uncover()
        self.covered_point = self.nearest_active_point(x, y)
        if self.covered_point is not None:
            self.covered_point.cover()

    def nearest_active_point(self, x, y):
        for line in self.points:
            for point in line:
                if dist(x, y, point.x, point.y) < Config.Field.VICINITY_DIST:
                    if point.active:
                        return point
                    else:
                        return None
        return None

    def draw_hull(self, hull, points):
        print(points)
        for i in range(len(points)):
            for j in range(len(points)):
                self.points[i][j].color = color[points[j][i].color]
                self.points[i][j].active = points[j][i].is_active
                if self.points[i][j].color != Config.Point.UNUSED_COLOR:
                    self.points[i][j].active = False
                self.points[i][j].update()
        # clear
        for obj in self.hulls:
            self.delete(obj)
        self.hulls.clear()
        for (i, j) in hull:
            pointa = self.points[i[1]][i[0]]
            pointb = self.points[j[1]][j[0]]
            self.hulls.append(self.create_line(pointa.x, pointa.y, pointb.x, pointb.y, fill=pointa.color, width=2))
