# draw a square
import turtle as t
t.pensize(10)
t.color('#9ACD32', '#FFF68F')
t.begin_fill()
for i in range(4):
    t.fd(100)
    t.left(90)
t.end_fill()
t.done()