from tkinter import *
from config import *
from random import randint
from button import *


class GameMenu(Canvas):
    def __init__(self, master):
        self.locked = False
        self.size = Config.GameMenu.SIZE
        col = Config.GUI.COLOR
        colp = Config.GameMenu.COLORPRESS
        colfg = Config.GameMenu.COLORFG
        n = Config.Field.CELL_COUNT
        l = Config.Field.CELL_SIZE
        fnt = Config.GameMenu.FONT
        self.hsize = (n + 1) * l
        k = 53
        b = 50
        a = k - 27
        c = k + 142
        self.r = Config.Sph.r
        self.ind = 10
        self.lef = self.ind
        self.rig = self.size - self.ind - self.r

        self.you = 'PL1: '
        self.op = 'PL2: '
        super().__init__(master, width=self.size, height=self.hsize, bg=col, highlightthickness=0)
        self.lb = Label(self, bg=col, fg=colfg, font=fnt, text='Score')
        self.lba = Label(self, bg=col, fg=colfg, font=fnt)
        self.lbb = Label(self, bg=col, fg=colfg, font=fnt)
        #self.lbc = Label(self, bg=col, fg=colfg, font='Ubuntu 41', text='Concede')

        #self.lbc.bind('<ButtonPress-1>', press)
        #self.lbc.bind('<ButtonRelease-1>', )

        self.lb.place(x=0, y=-6)
        self.lba.place(x=0, y=70)
        self.lbb.place(x=0, y=145)

        self.score(0, 0)

    def score(self, a, b):
        self.lba['text'] = self.you + str(a)
        self.lbb['text'] = self.op + str(b)

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

def pressb(event):
    event.widget.press()

def releaseb(event):
    event.widget.release()
