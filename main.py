from tkinter import *

from point import Point

from random import randint


class StartMenu(Toplevel):
    def __init__(self, master):
        super().__init__(master, bg='green')
        self.title('POP-go')
      #  self.resizable(width=False, height=False)
        def press(event):
            master.deiconify()
            self.destroy()
        self.lbl = Label(self, text='Play', bg='red', font='Consolas 50', \
                        )

        self.lbl.pack()
        self.lbl.bind('<Button-1>', press)


root = Tk()
root.withdraw()
sm = StartMenu(root)
root.title("POP-GO")
root.resizable(height=False, width=False)

canv = Canvas(root, width=680, height=720, bg='white')

canv.pack()
canv.create_rectangle(20, 20, 660, 660, fill="white", outline="black", width=3)
canv.delete(None)
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

def run():
    points[randint(0, len(points) - 1)].cover()
    root.after(1, run)

run()
root.mainloop()


