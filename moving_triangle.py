from tkinter import *
import time


tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
my_triangle = canvas.create_polygon(30, 10, 20, 40, 40, 40, fill="green", outline="black")
for x in range(0, 60):
    canvas.move(my_triangle, 5, 0)
    canvas.update()
    time.sleep(0.05)
for x in range(0, 60):
    canvas.move(my_triangle, 0, 5)
    canvas.update()
    time.sleep(0.05)
for x in range(0, 60):
    canvas.move(my_triangle, -5, 0)
    canvas.update()
    time.sleep(0.05)
for x in range(0, 60):
    canvas.move(my_triangle, 0, -5)
    canvas.update()
    time.sleep(0.05)
tk.mainloop()



