from tkinter import *
from config import *


class StartMenu(Toplevel):
    def __init__(self, master):
        self.master = master
        self.col = Config.GUI.COLOR
        self.colfg = Config.StartMenu.COLORFG
        fnt = Config.StartMenu.FONT
        geom = Config.StartMenu.GEOM
        super().__init__(master, bg=self.col)
        self.geometry(Config.StartMenu.GEOM)
        self.title('POP-go')
        self.overrideredirect(1)
        self.resizable(width=False, height=False)
        self.x = Config.StartMenu.GEOMX
        self.y = Config.StartMenu.GEOMY
        self.indx = 70
        self.indy = 100
        self.indyinf = 44
        yt = 64
        self.r = Config.StartMenu.R

        self.canv = Canvas(self, width=500, height=200, highlightthickness=0, bg=self.col)
        self.canv.place(x=0, y=0)

        lbp = Label(self, bg=self.colfg, fg=self.col, font=fnt, text='POP-GO')
        lbp.place(x=self.x/2, y=yt, anchor='center')

        self.inflb = Label(self, bg=self.col, fg='gray', font='inconsolata 25', text='loading...')
        self.inflb.place(x=self.x / 2, y=self.y-self.indyinf, anchor='center')

        self.canv.create_rectangle(self.indx, 0, self.x-self.indx, self.y-self.indy,
                                   fill=self.colfg, outline=self.colfg)
        self.canv.create_oval(self.indx, self.y-self.indy-self.r, self.indx + 2 * self.r,
                              self.y-self.indy+self.r, fill=self.colfg, outline=self.colfg)
        self.canv.create_oval(self.x-self.indx-2*self.r, self.y - self.indy - self.r, self.x-self.indx,
                              self.y - self.indy + self.r, fill=self.colfg, outline=self.colfg)
        self.canv.create_rectangle(self.indx+self.r, self.y-self.indy + self.r, self.x - self.indx-self.r, self.y - self.indy,
                                   fill=self.colfg, outline=self.colfg)

    def report(self, s):
        if s == 'Game is Starting Now':
            def exit_menu():
                self.master.deiconify()
                self.destroy()
            self.after(2000, exit_menu)
        self.inflb.config(text=s)

