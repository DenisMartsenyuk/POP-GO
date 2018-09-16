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
        self.colbg = Config.GameMenu.COLORBG
        self.colp = Config.GameMenu.COLORPRESS
        self.col = Config.GameMenu.COLORTEXT
        self.colfg = Config.GameMenu.COLORFG
        self.fnt = Config.GameMenu.FONT
        self.root = rt
        n = Config.Field.CELL_COUNT
        l = Config.Field.CELL_SIZE
        self.hsize = (n + 1) * l
        self.r = Config.Sph.r
        self.ind = 10
        self.lef = self.ind
        self.rig = self.size - self.ind - self.r
        self.colc = 'red'
        super().__init__(master, fg=self.col, bg=self.colbg, font='BebasNeue 31', text='Concede')

        self.sph1 = rt.create_oval(self.lef - 2, self.hsize - self.r - 1, self.lef - 2 + self.r, self.hsize - 1, width=1,
                                     fill=self.colbg, outline=self.colbg)
        self.sph2 = rt.create_oval(self.rig, self.hsize - self.r - 1, self.rig + self.r, self.hsize - 1, width=1,
                                   fill=self.colbg, outline=self.colbg)
        self.rect = rt.create_rectangle(self.lef - 2 + self.r/2, self.hsize - self.r - 1, self.rig - 2 + self.r/2,
                                        self.hsize - 1, width=1, fill=self.colbg, outline=self.colbg)

    def press(self):
        self.root.itemconfig(self.sph1, fill=self.colp, outline=self.colp)
        self.root.itemconfig(self.sph2, fill=self.colp, outline=self.colp)
        self.root.itemconfig(self.rect, fill=self.colp, outline=self.colp)
        self['bg']=self.colp

    def release(self):
        self.root.itemconfig(self.sph1, fill=self.colbg, outline=self.colbg)
        self.root.itemconfig(self.sph2, fill=self.colbg, outline=self.colbg)
        self.root.itemconfig(self.rect, fill=self.colbg, outline=self.colbg)
        self['bg'] = self.colbg
