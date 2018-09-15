from tkinter import *
from config import Config


class StartMenu(Toplevel):
    col=Config.StartMenu.COLOR
    def __init__(self, master):
        super().__init__(master, bg=col)
        self.title('POP-go')
        self.geometry('200x100+500+500')
        self.overrideredirect(1)
        self.resizable(width=False, height=False)

        def press(event):
            master.deiconify()
            self.destroy()
        self.lbl = Label(self, text='Play', bg='red', font='Consolas 50')

        self.lbl.pack()
        self.lbl.bind('<Button-1>', press)

