import turtle
import time

POSPONER = 0.1

#Configuracion de la ventana principal
ventana = turtle.Screen()
ventana.title("Snake EDD")
ventana.bgcolor("white")
ventana.setup(width = 520, height = 520)
ventana.tracer(0)

#Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.shapesize(stretch_wid=2, stretch_len=2) 
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"
cabeza.color("pink")

#Funciones para la direccion
def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def derecha():
    cabeza.direction = "right"

def izquierda():
    cabeza.direction = "left"

#Funciones para el movimiento
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 40)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 40)
    
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 40)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 40)

#Configuracion del teclado
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(derecha, "Right")
ventana.onkeypress(izquierda, "Left")

#Bucle principal
while True:
    ventana.update()

    mov()
    time.sleep(POSPONER)

#Funcion para ejecutar la ventana
ventana.mainloop()