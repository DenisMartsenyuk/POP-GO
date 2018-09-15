from tkinter import *

from point import Point
from start_menu import StartMenu
from field import Field
from game_menu import GameMenu


root = Tk()
root.withdraw()
sm = StartMenu(root)
root.title("POP-GO")
root.resizable(height=False, width=False)


field = Field(root, 100)
'''canv = Canvas(root, width=680, height=720, bg='white')

canv.pack()
canv.create_rectangle(20, 20, 660, 660, fill="white", outline="black", width=3)

for i in range(32):
    canv.create_line(i * 20 + 20, 20, i * 20 + 20, 660, width=1)
    canv.create_line(20, i * 20 + 20, 660, i * 20 + 20, width=1)


points = []

for i in range(1, 32):
    for j in range(1, 32):
        x = 20 + 20 * i
        y = 20 + 20 * j
        points.append(Point(canv, x, y, 2, 'red'))


for i in points:
    i.draw()
'''
root.mainloop()


