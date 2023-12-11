import turtle
import random

s = turtle.Screen()

s.title("Primer Proyecto")
s.bgcolor("pink")

jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()
jugador3 = turtle.Turtle()

jugador1.hideturtle()
jugador1.shape("turtle")
jugador1.color("red","red")
jugador1.shapesize(2,2,2)
jugador1.pensize(3)

jugador2.hideturtle()
jugador2.shape("turtle")
jugador2.color("blue","blue")
jugador2.shapesize(2,2,2)
jugador2.pensize(3)

jugador3.hideturtle()
jugador3.shape("turtle")
jugador3.color("green","green")
jugador3.shapesize(2,2,2)
jugador3.pensize(3)

jugador1.penup()
jugador1.goto(200, 200)
jugador1.pendown()
jugador1.speed(10)
jugador1.circle(45)

jugador1.penup()
jugador1.goto(-250, 225)
jugador1.showturtle()

jugador2.penup()
jugador2.goto(200, -200)
jugador2.pendown()
jugador2.speed(10)
jugador2.circle(45)


jugador2.penup()
jugador2.goto(-250,-170)
jugador2.showturtle()

jugador3.penup()
jugador3.goto(200, 0)
jugador3.pendown()
jugador3.speed(10)
jugador3.circle(45)


jugador3.penup()
jugador3.goto(-250, 25)
jugador3.showturtle()

dado = [1,2,3,4,5,6]


for i in range(20):
      if jugador1.pos() > (190,200):
            print("latortuga Roja ha ganado") 
            break
      elif jugador2.pos() > (190, -200):
            print("la tortuga Azul ha ganado")
            break
      elif jugador3.pos() > (190, 0):
            print("la tortuga Verde ha gananado")
            break
      else:
          turno1 = input("Presiona la tecla enter para avanzar")
          turno1 = random.choice(dado)
          print("tu número es: ",turno1,"\nAvanzas: ",turno1*20)
          jugador1.pendown()
          jugador1.fd(20*turno1)
          
          turno2 = input("Presiona la tecla enter para avanzar la tortuga azul.")
          turno2 = random.choice(dado)
          print("Tu número es: ",turno2,"\nAvanzas:", turno2*20)
          jugador3.pendown()
          jugador3.fd(20*turno2)

          turno3 = input("Presiona la tecla enter para avanzar 1")
          turno3 = random.choice(dado)
          print("Tu numero es: ",turno3,"\nAvanzas:", turno3*20)
          jugador2.pendown()
          jugador2.fd(20*turno3)
      
      
     
turtle.done()