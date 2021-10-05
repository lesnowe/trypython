import turtle as t
t1 = t.Turtle()
t1.pensize(2)
t1.color('blue', 'yellow')
t1.begin_fill()
for i in range(6):
    t1.fd(100)
    t1.left(60)
t1.end_fill()
t.done()