import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.speed(9)
t.circle(100)
t.circle(50)
t.circle(10)
t.dot(3)

t.hideturtle()
t.speed(1)
t.circle(40)
t.showturtle()
t.circle(60)

t.setx(100)
t.sety(-300)

turtle.done()