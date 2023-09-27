import turtle
import time
import random

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
cabeza.color("green4")

#Manzanas para la serpiente
manzana = turtle.Turtle()
manzana.speed(0)
manzana.shape("circle")
manzana.shapesize(stretch_wid=2, stretch_len=2) 
manzana.penup()
manzana.goto(100,150)
manzana.color("red")

#Ubicacion manzana
def ubicarManzana():
    while True:
        x = random.randint(-240,240)
        y = random.randint(-240,240)
        sobrep = False

        if cabeza.distance(x,y) <= 40:
            continue
        for cuadro in cuerpo:
            if cuadro.distance(x,y) <= 40:
                sobrep = True
                break
        if sobrep:
            continue
        else:
            manzana.goto(x,y)
            break

#Cuerpo de la serpiente
cuerpo = []
for i in range(1,3):
    cuadro = turtle.Turtle()
    cuadro.speed(0)
    cuadro.shape("square")
    cuadro.shapesize(stretch_wid=2, stretch_len=2) 
    cuadro.penup()
    cuadro.goto(0,-40*i)
    cuadro.direction = "stop"
    cuadro.color("green3")
    cuerpo.append(cuadro)

#Funciones para la direccion
def arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"

def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"

def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

def izquierda():
    if cabeza.direction != "right":
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

    #Interaccion bordes
    if cabeza.xcor() > 240 or cabeza.xcor() < -240 or cabeza.ycor() > 240 or cabeza.ycor() < -240:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        manzana.goto(100,150)

        #Eliminar cuerpo
        for s in cuerpo:
            s.goto(2000,2000)
        #Eliminar de la lista
        cuerpo.clear()

        for i in range(1,3):
                cuadro = turtle.Turtle()
                cuadro.speed(0)
                cuadro.shape("square")
                cuadro.shapesize(stretch_wid=2, stretch_len=2) 
                cuadro.penup()
                cuadro.goto(0,-40*i)
                cuadro.direction = "stop"
                cuadro.color("green3")
                cuerpo.append(cuadro)

    if cabeza.direction != "stop":
        #Interraccion de la serpiente con las manzanas
        if cabeza.distance(manzana) < 40:
            ubicarManzana()

            ncuadro = turtle.Turtle()
            ncuadro.speed(0)
            ncuadro.shape("square")
            ncuadro.shapesize(stretch_wid=2, stretch_len=2) 
            ncuadro.penup()
            ncuadro.color("green3")
            cuerpo.append(ncuadro)
            
        #Movimiento del cuerpo de la serpiente
        cuadros = len(cuerpo)
        for i in range(cuadros-1, 0, -1):
            x = cuerpo[i-1].xcor()
            y = cuerpo[i-1].ycor()
            cuerpo[i].goto(x,y)

        if cuadros>0:
            x = cabeza.xcor()
            y = cabeza.ycor()
            cuerpo[0].goto(x,y)

    mov()

    #Colisiones con el cuerpo de la serpiente
    for c in cuerpo:
        if c.distance(cabeza) < 40:
            time.sleep(0.5)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            manzana.goto(100,150)

            #Eliminar cuerpo
            for k in cuerpo:
                k.goto(2000,2000)
                
            cuerpo.clear()
            for i in range(1,3):
                cuadro = turtle.Turtle()
                cuadro.speed(0)
                cuadro.shape("square")
                cuadro.shapesize(stretch_wid=2, stretch_len=2) 
                cuadro.penup()
                cuadro.goto(0,-40*i)
                cuadro.direction = "stop"
                cuadro.color("green3")
                cuerpo.append(cuadro)

    time.sleep(POSPONER)

#Funcion para ejecutar la ventana
ventana.mainloop()