import turtle

s = turtle.Screen()
t = turtle.Turtle()
i = 0

'''t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)'''

'''for i in range(4):
    t.forward(100)
    t.rt(90)
    
for i in range(4):
    t.forward(200)
    t.rt(90)'''
     
'''t.circle(100)
t.circle(90)
t.circle(80)
t.circle(70)
t.circle(60)
t.circle(50)
t.circle(40)'''

resultado = input("¿Quieres imprimir un objeto?")
if resultado == "si":
    while i <= 100:
          t.circle(i)
          i += 10

else:
   print("oka")


turtle.done()
