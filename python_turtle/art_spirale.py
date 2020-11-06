

import turtle

colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']

test = turtle.Pen()
turtle.bgcolor('gray')
test.speed(0)

for x in range(300):
    test.pencolor(colors[x % 6])
    test.width(x/100+1)
    test.forward(x)
    test.left(59)

turtle.done()
