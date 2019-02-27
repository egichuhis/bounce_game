from tkinter import *
import time

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
my_image = PhotoImage(file='c:\\explosion.gif')
my_images = canvas.create_image(0, 0, anchor=NW, image=my_image)
for x in range(0, 60):
    canvas.move(my_images, 5, 0)
    canvas.update()
    time.sleep(0.05)
tk.mainloop()