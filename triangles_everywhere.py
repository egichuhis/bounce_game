from tkinter import *
import random

w = 400
h = 400
tk = Tk()
canvas = Canvas(tk, width=w, height=h)
canvas.pack()


def random_triangle():
    x1 = random.randrange(w)
    y1 = random.randrange(h)
    x2 = random.randrange(w)
    y2 = random.randrange(h)
    x3 = random.randrange(w)
    y3 = random.randrange(h)
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="", outline="black")


for x in range(0, 100):
    random_triangle()
tk.mainloop()