from tkinter import *
from config import *
from random import randint

class GameMenu(Canvas):
    def __init__(self, master):
        size = Config.GameMenu.SIZE
        col = Config.GameMenu.COLOR
        n = Config.Field.CELL_COUNT
        l = Config.Field.CELL_SIZE
        a = randint(0, 100)
        b = randint(0, 100)

        hsize = (n + 1) * l
        super().__init__(master, width=size, height=hsize, highlightthickness=0)
        #frm=Frame(self, height=50, width=size, bd=2, bg='red')
        self.create_rectangle(0, 0, size, hsize, fill=col, width=0)
        self.lb = Label(self, bg='white', fg='#f06c00', width=6, font='OldEnglishTextMT 43', text='Score :',
                        justify=LEFT)
        self.lba = Label(self, bg='white', fg='#f06c00', font='OldEnglishTextMT 43')
        self.lbb = Label(self, bg='white', fg='#f06c00', font='OldEnglishTextMT 43')
        self.lb.grid(row=0, column=0, sticky=W)
        self.lba.grid(row=1, column=0, sticky=W)
        self.lbb.grid(row=2, column=0, sticky=W)
        self.you = 'You: '
        self.op = 'Enemy: '
        self.score(a, b)
        #frm.pack()

    def score(self, a, b):
        self.lba['text'] = self.you + str(a)
        self.lbb['text'] = self.op + str(b)