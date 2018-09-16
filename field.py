from tkinter import *

from point import Point
from config import *

import math


def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

colors = {-1: Config.Point.PLAYER2_COLOR, 0: Config.Point.UNUSED_COLOR, 1: Config.Point.PLAYER1_COLOR}


class Field(Canvas):
    def __init__(self, master, choose_point_callback=None):
        n = Config.Field.CELL_COUNT
        l = Config.Field.CELL_SIZE
        field_size = (n + 1) * l
        super().__init__(master, width=field_size, height=field_size,
                         bg='gray', highlightthickness=0)
        self.focus_set()
        # draw border
        self.create_rectangle(1, 1, field_size - 1, field_size - 1, fill=Config.Field.CANV_COLOR, width=2)

        # draw sharp
        for i in range(n + 1):
            self.create_line(l * i, 0, l * i, field_size)
            self.create_line(0, l * i, field_size, l * i)

        self.points = [[None] * n for i in range(n)]
        for j in range(n):
            for i in range(n):
                self.points[i][j] = Point(self, l * (i + 1), l * (j + 1), Config.Point.RADIUS, Config.Point.UNUSED_COLOR)
                self.points[i][j].draw()

        self.covered_point = None
        self.bind('<Motion>', lambda e: self.handle_covered_point(e.x, e.y))

        def press(event):
            if not self.locked:
                point = self.nearest_active_point(event.x, event.y)
                print(point)
                if point is not None:
                    choose_point_callback(point.y // Config.Field.CELL_SIZE - 1, point.x // Config.Field.CELL_SIZE - 1)

        self.bind('<Button-1>', press)
        self.hulls = []
        self.locked = False

    def handle_covered_point(self, x, y):
        if not self.locked:
            if self.covered_point is not None:
                self.covered_point.uncover()
            self.covered_point = self.nearest_active_point(x, y)
            if self.covered_point is not None:
                self.covered_point.cover()

    def nearest_active_point(self, x, y):
        for line in self.points:
            for point in line:
                if dist(x, y, point.x, point.y) < Config.Field.VICINITY_DIST:
                    if point.is_active:
                        return point
                    else:
                        return None
        return None

    def display(self, hull, points):
        for i in range(len(points)):
            for j in range(len(points)):
                self.points[i][j].color = colors[points[j][i].color]
                self.points[i][j].is_active = points[j][i].is_active # for points in hull
                if self.points[i][j].color != Config.Point.UNUSED_COLOR:
                    self.points[i][j].is_active = False
                    self.points[i][j].is_visible = True
                self.points[i][j].update()
        # clear
        for obj in self.hulls:
            self.delete(obj)
        self.hulls.clear()

        for (i, j) in hull:
            point_a = self.points[i[1]][i[0]]
            point_b = self.points[j[1]][j[0]]
            self.hulls.append(self.create_line(point_a.x, point_a.y, point_b.x, point_b.y, fill=point_a.color, width=2))

    def lock(self):
        print('Locked fld')
        self.locked = True
        if self.covered_point is not None:
            self.covered_point.uncover()

    def unlock(self):
        print('Unclock fld')
        self.locked = False
