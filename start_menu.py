from tkinter import *
from config import *


class StartMenu(Toplevel):
    def __init__(self, master):
        col = Config.StartMenu.COLOR
        super().__init__(master, bg=col)
        self.geometry('600x200+500+400')


        #frm=Frame(self, height=200, width=650, bg=col)
        #frm.pack()

        lbw = Label(self, bg=col, fg='#f06c00', font='OldEnglishTextMT 40', text='Welcome')
        lbt = Label(self, bg=col, fg='#f06c00', font='OldEnglishTextMT 32', text='to')
        lbp = Label(self, bg='gray', fg='#f06c00', font='OldEnglishTextMT 64', text='POP-GO')
        #lbw.pack()
        #lbt.pack()
        lbp.pack()
        self.title('POP-go')
        self.overrideredirect(1)
        self.resizable(width=False, height=False)

        def press(event):
            master.deiconify()
            self.destroy()

        self.bind('<Button-1>', press)

