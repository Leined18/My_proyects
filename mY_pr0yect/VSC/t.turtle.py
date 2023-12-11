import turtle 
import math
t = turtle.Turtle
s = turtle.Screen
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
            math.cos(2*k)-2*\
            math.cos(3*k)-\
            math.cos(4*k)

turtle.bgcolor("black")
for i in range(10000):
    t.goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        t.color("#f72460")
    t.goto(0,0)
turtle.done()
     
      