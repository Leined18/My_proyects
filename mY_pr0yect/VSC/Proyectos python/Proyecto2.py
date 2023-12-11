import turtle 
import time
import random


retraso = 0.1
marcador = 0
marcador_alto = 0


screen = turtle.Screen()
screen.setup(650,650)
screen.bgcolor("gray")
screen.title('Proyecto 2')


       




snake = turtle.Turtle()
snake.speed(1)
snake.shape('square')
snake.penup()
snake.goto(0,0) 
snake.direction = 'left'
snake.color('black','green')

comida = turtle.Turtle()
comida.shape("circle")
comida.color("black","orange")
comida.penup()
comida.goto(0,100)
comida.speed(0)

comida2 = turtle.Turtle()
comida2.shape("circle")
comida2.color("black", "red")
comida2.penup()
comida2.goto(5,-100)
comida2.speed(0)

body = []

text = turtle.Turtle()
text.speed(0)
text.color("black")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write("Marcador: 0\tMarcador más alto: 0", align="center", font=("verdana", 20,"normal"))

#snake
def arriba():
    snake.direction = "up"

def abajo():
    snake.direction = "down"

def derecha():
    snake.direction = "right"

def izquierda():
    snake.direction = "left"


#snake
def movimiento():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)


screen.listen()
screen.onkeypress(arriba, "Up")
screen.onkeypress(abajo, "Down")
screen.onkeypress(izquierda, "Left")
screen.onkeypress(derecha, "Right")







while True:
    screen.update()

    if snake.xcor() > 300 or snake.xcor( ) < -300 or snake.ycor() > 300 or snake.ycor( ) < -300:
         time.sleep(2)
         for i in body:
                i.clear()
                i.hideturtle()
                snake.home()                
                snake.direction = "stop"
                body.clear()

                marcador = 0
                text.clear()
                text.write("Marcador:{}\tMarcador más alto:{}".format(marcador,marcador_alto),align="center", font=("verdana", 20, "normal"))



        
 

    if snake.distance(comida) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        comida.goto(x,y)

        new_body = turtle.Turtle()
        new_body.shape("square")
        new_body.color("black","green")
        new_body.penup()
        new_body.goto(0,0)
        new_body.speed(0)
        body.append(new_body)

        marcador += 10
        if marcador > marcador_alto:
            marcador_alto = marcador
            text.clear()
            text.write("Marcador:{}\tMarcador más alto:{}".format(marcador,marcador_alto),align="center", font=("verdana", 20, "normal"))

    total = len(body)
    for index in range(total -1, 0, -1):
      x = body[index-1].xcor()
      y = body[index-1].ycor()
      body[index].goto(x,y)

    if total > 0:
      x = snake.xcor()
      y = snake.ycor()
      body[0].goto(x,y) 
    
    
    if snake.distance(comida2) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        comida2.goto(x,y)

        new_body = turtle.Turtle()
        new_body.shape("square")
        new_body.color("black","green")
        new_body.penup()
        new_body.goto(0,0)
        new_body.speed(0)
        body.append(new_body)


           
    movimiento()

    for i in body:
        if i.distance(snake) < 20:

            time.sleep(0.5)
            for i in body:
                i.clear()
                i.hideturtle()
            snake.home()
            body.clear()
            snake.direction = "stop"

            marcador = 0
            text.clear()
            text.write("Marcador:{}\tMarcador más alto:{}".format(marcador,marcador_alto),align="center", font=("verdana", 20, "normal"))

    time.sleep(retraso)
    if marcador == 20:
        screen.bgcolor("violet")

    if marcador == 30:
        screen.bgcolor("purple")
       

    if marcador == 50:
        screen.bgcolor("lime")
      
    
    if marcador == 70:
        screen.bgcolor("cyan")
       

    if marcador == 80:
        screen.bgcolor("blue")
        snake.speed(1)
        
        screen.bgcolor("cyan")
        
        
    if marcador == 100:
        screen.bgcolor("blue")
        
  
    if marcador == 0:
        screen.bgcolor("gray")
        snake.speed(10)
        

turtle.done()
