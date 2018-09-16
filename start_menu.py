from tkinter import *
from config import *


class StartMenu(Toplevel):
    def __init__(self, master):
        col = Config.GUI.COLOR
        colfg = Config.StartMenu.COLORFG
        fnt = Config.StartMenu.FONT
        geom = Config.StartMenu.GEOM
        super().__init__(master, bg=col)
        self.geometry('600x170+500+400')
        self.title('POP-go')
        self.overrideredirect(1)
        self.resizable(width=False, height=False)

        lbp = Label(self, bg=col, fg=colfg, font=fnt, text='POP-GO')
        lbp.pack()

        def press(event):
            master.deiconify()
            self.destroy()

        self.bind('<Button-1>', press)

