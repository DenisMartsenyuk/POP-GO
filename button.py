from tkinter import *
from config import *

def press(event):
    event.widget.color = 'black'
    event.widget.update()

def hide(event):
    event.widget.color = 'gray'
    event.widget.update()

class But(Label):
    def __init__(self, master, rt):
        self.size = Config.GameMenu.SIZE
        self.col = Config.GUI.COLOR
        self.colp = Config.GameMenu.COLORPRESS
        self.colfg = Config.GameMenu.COLORFG
        self.fnt = Config.GameMenu.FONT
        self.root = rt
        n = Config.Field.CELL_COUNT
        l = Config.Field.CELL_SIZE
        self.hsize = (n + 1) * l
        self.k = 53
        self.b = 50
        self.a = self.k - 27
        self.c = self.k + 142
        self.colc = 'red'
        super().__init__(master, fg=self.colfg, bg=self.col, font='Ubuntu 41', text='Concede')

        self.sph1 = rt.create_oval(self.a, self.hsize - 52 - 0.5, self.a + self.b, self.hsize - 1, width=1,
                                   fill=self.col, outline=self.col)
        self.sph2 = rt.create_oval(self.c, self.hsize - 52 - 0.5, self.c + self.b, self.hsize - 1, width=1,
                                   fill=self.col, outline=self.col)

    def press(self):
        self.root.itemconfig(self.sph1, fill=self.colp, outline=self.colp)
        self.root.itemconfig(self.sph2, fill=self.colp, outline=self.colp)
        self['bg']=self.colp

    def release(self):
        self.root.itemconfig(self.sph1, fill=self.col, outline=self.col)
        self.root.itemconfig(self.sph2, fill=self.col, outline=self.col)
        self['bg'] = self.col
