import turtle 

s = turtle.Screen()
t = turtle.Turtle()

'''Triangle'''
t.goto(100,100)
t.goto(-100,100)
'''t.goto(0,0)'''
t.home() 

'''Rectangle'''
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)
t.right(90)
t.forward(100)
t.rt(90)
t.fd(100)


turtle.done()