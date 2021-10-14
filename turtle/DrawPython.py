import turtle as t
t.pensize(30)
t.pencolor('purple')
t.penup()
t.setpos(-250,0)
t.pendown()
t.seth(-40)
for i in range(4):
    t.circle(40, 80)
    t.circle(-40, 80)
t.seth(0)
t.circle(40,180)
t.fd(50)
t.done()