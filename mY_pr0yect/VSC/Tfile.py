import turtle 
import random
import time

dado_x = [1,2,5]
dado = [1,2,3,5,6,7,8]

multicolor = ["green","yellow","red","blue","violet","orange","lime","pink","cyan"]
t = turtle.Turtle()
t2 = turtle.Turtle()
s = turtle.Screen()
i = 1
# posicion montaña 1
x = -200
y = 200
# posicion montaña 2
x2 = 200
y2 = 200
# avance
f = 10


# montaña 1

t.hideturtle()
t.pencolor("black")
t.speed(10)
# montaña 2 

t2.hideturtle()
t2.pencolor("black")
t2.speed(10)


# procesos
for i in range(200):     
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fd(f)
    y -= 1
    x -= random.choice(dado_x)
    
    t2.penup()
    t2.goto(x2,y2)
    t2.pendown()
    t2.fd(f)
    y2 -= 1
    x2 -= random.choice(dado_x)
    f += random.choice(dado) 


turtle.done()
