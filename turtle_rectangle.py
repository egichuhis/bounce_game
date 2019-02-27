import turtle

t = turtle.Pen()

t.begin_fill()
t.color(1, 1, 0)
for x in range(1, 9):
    t.forward(100)
    t.left(45)
t.end_fill()
"""
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)

"""

turtle.done()