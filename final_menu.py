from tkinter import *

from config import *

class FinalMenu(Tk):
    def __init__(self, text):
        super().__init__()
        self.overrideredirect(1)
        self.resizable(width=False, height=False)

        self.col = Config.GUI.COLOR
        self.colfg = Config.StartMenu.COLORFG
        fnt = Config.StartMenu.FONT
        geom = Config.StartMenu.GEOM

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

        lbp = Label(self, bg=self.colfg, fg=self.col, font=fnt, text=text)
        lbp.place(x=self.x / 2, y=yt, anchor='center')

        self.canv.create_rectangle(self.indx, 0, self.x - self.indx, self.y - self.indy,
                                   fill=self.colfg, outline=self.colfg)
        self.canv.create_oval(self.indx, self.y - self.indy - self.r, self.indx + 2 * self.r,
                              self.y - self.indy + self.r, fill=self.colfg, outline=self.colfg)
        self.canv.create_oval(self.x - self.indx - 2 * self.r, self.y - self.indy - self.r, self.x - self.indx,
                              self.y - self.indy + self.r, fill=self.colfg, outline=self.colfg)
        self.canv.create_rectangle(self.indx + self.r, self.y - self.indy + self.r, self.x - self.indx - self.r,
                                   self.y - self.indy,
                                   fill=self.colfg, outline=self.colfg)

        self.after(5000, lambda: self.destroy())
        self.mainloop()
