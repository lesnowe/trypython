# draw a square
import turtle as t
t.pensize(10)
t.pencolor('#9ACD32')
t.begin_fill()
for i in range(4):
    t.fd(100)
    t.left(90)
t.fillcolor('#FFF68F')
t.end_fill()
t.done()