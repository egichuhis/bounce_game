from tkinter import *


tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_text(150, 100, text='Who rode around on a moose', fill="red", font=('Times', 15))
tk.mainloop()