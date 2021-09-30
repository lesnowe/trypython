import turtle as t
t.pensize(3)
t.left(100)
t.fd(120)
while True:
    t.right(80)
    t.fd(120)
    if abs(t.pos()) < 1:
        break
t.done()