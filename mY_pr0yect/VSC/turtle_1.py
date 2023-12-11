import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("Violet")

t.hideturtle()
t.shapesize(5,5,5)
t.color("purple","blue")
t.shape("turtle")


t.penup()
t.goto(-200,100)
t.pendown()
t.circle(90)

t.showturtle()
t.speed(1)
t.fd(500)
t.pos()



s.bgcolor("Purple")

t.color("blue","violet")



turtle.done()