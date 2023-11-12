import turtle
import time
import random
from collections import deque

import tkinter as tk

POSPONER = 0.08
contador_movimientos = 0
aleatorio=0

#Funcion para la ventana de informacion general
def informacion():    
    # Crear la ventana
    info = tk.Tk()
    info.title("Informacion general")   
    info.config(background="khaki") 

    # Obtener el tamaño de la pantalla
    anchoPantalla = info.winfo_screenwidth()
    altoPantalla = info.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana
    x = (anchoPantalla - 400) // 2  # Ancho de la ventana
    y = (altoPantalla - 300) // 2   # Alto de la ventana
    
    
    info.geometry("400x300+{}+{}".format(x, y))

    # Crear un título
    titulo = tk.Label(info, text="Juego Snake Master 4.0 :) ", font=("Arial", 18))
    titulo.pack(pady=25) 
    titulo.config(background="skyblue2") 

    # Crear un párrafo de texto
    texto = """
    ▶ Controles: las fechas del teclado  ← → ↑ ↓

    ▶ Para inciar con el juego cierra esta ventana 
    dando clic en la ✘ superior

    ¡Come la mayor cantidad de frijolitos que puedas!
    """
    parrafo = tk.Label(info, text=texto, font=("Arial", 12), justify="left")
    parrafo.pack(pady=10) 
    parrafo.config(background="khaki") 

    # Iniciar el bucle principal de la ventana
    info.mainloop()

#Funcion para el mensaje de GAME OVER
def mensaje_gameOver():
    # Crear la ventana
    lose = tk.Toplevel()
    lose.title("Mensaje de Game Over") 
    lose.config(background="red")

    # Obtener el tamaño de la pantalla
    anchoPantalla = lose.winfo_screenwidth()
    altoPantalla = lose.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana
    x = (anchoPantalla - 300) // 2  # Ancho de la ventana
    y = (altoPantalla - 200) // 2   # Alto de la ventana
    
    
    lose.geometry("300x200+{}+{}".format(x, y))

    # Crear un título
    mensaje = tk.Label(lose, text="Game Over :( ", font=("Arial", 23) )
    mensaje.pack(pady=60)      
    mensaje.config(background="red", fg="white")

#Funcion que ejecuta el juego
def juego():
    global aleatorio
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
    cabeza.color("SeaGreen1")

    #Manzanas para la serpiente
    manzana = turtle.Turtle()
    manzana.speed(0)
    manzana.shape("circle")
    manzana.shapesize(stretch_wid=2, stretch_len=2) 
    manzana.penup()
    manzana.goto(100,150)
    manzana.color("red")

    # Función para incrementar el contador de movimientos
    def incrementar_contador():
        global contador_movimientos
        contador_movimientos = (contador_movimientos % 10) + 1  # Reinicia a 1 cuando llega a 10

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
    cuerpo = deque()
    for i in range(-2,0):
        cuadro = turtle.Turtle()
        cuadro.speed(0)
        cuadro.shape("square")
        cuadro.shapesize(stretch_wid=2, stretch_len=2) 
        cuadro.penup()
        cuadro.goto(0, 40*i)
        cuadro.direction = "stop"
        cuadro.color("green3")
        cuerpo.append(cuadro)

    #Funciones para la direccion
    def arriba():
        global contador_movimientos

        if cabeza.direction != "down":
            cabeza.direction = "up"
            incrementar_contador()

    def abajo():
        global contador_movimientos
        if cabeza.direction != "up" and cabeza.direction != "stop":
            cabeza.direction = "down"
            incrementar_contador()

    def derecha():
        global contador_movimientos
        if cabeza.direction != "left":
            cabeza.direction = "right"
            incrementar_contador()

    def izquierda():
        global contador_movimientos
        if cabeza.direction != "right":
            cabeza.direction = "left"
            incrementar_contador()

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

            #Muestra el mensaje de que perdio el juego
            mensaje_gameOver()
            
            for i in range(-2,0):
                    cuadro = turtle.Turtle()
                    cuadro.speed(0)
                    cuadro.shape("square")
                    cuadro.shapesize(stretch_wid=2, stretch_len=2) 
                    cuadro.penup()
                    cuadro.goto(0, 40*i)
                    cuadro.direction = "stop"
                    cuadro.color("green3")
                    cuerpo.append(cuadro)

        if cabeza.direction != "stop":
            
            #Interraccion de la serpiente con las manzanas            
            if cabeza.distance(manzana) < 40 :
                manzana.goto(300,300)
                aleatorio = random.randint(1, 10)
                

                ncuadro = turtle.Turtle()
                ncuadro.speed(0)
                ncuadro.shape("square")
                ncuadro.shapesize(stretch_wid=2, stretch_len=2) 
                ncuadro.penup()
                ncuadro.color("green3")
                x = cuerpo[-1].xcor()
                y = cuerpo[-1].ycor()
                cuerpo.append(ncuadro)
                ncuadro.goto(x,y)
                
            #Movimiento del cuerpo de la serpiente          
            x = cabeza.xcor()
            y = cabeza.ycor()
            c = cuerpo.popleft()
            cuerpo.append(c)
            c.goto(x,y)

            coordenadas = manzana.pos()
            if coordenadas[0] >= 300 and coordenadas[1] >= 300:
                if contador_movimientos == aleatorio:
                    ubicarManzana()

        mov()

        #Colisiones con el cuerpo de la serpiente
        for c in list(cuerpo):
            if c.distance(cabeza) < 40:
                time.sleep(0.5)
                cabeza.goto(0,0)
                cabeza.direction = "stop"
                manzana.goto(100,150)

                #Eliminar cuerpo
                for k in cuerpo:
                    k.goto(2000,2000)
                    
                cuerpo.clear()
                #Muestra el mensaje de que perdio el juego
                mensaje_gameOver()

                for i in range(-2,0):
                    cuadro = turtle.Turtle()
                    cuadro.speed(0)
                    cuadro.shape("square")
                    cuadro.shapesize(stretch_wid=2, stretch_len=2) 
                    cuadro.penup()
                    cuadro.goto(0, 40*i)
                    cuadro.direction = "stop"
                    cuadro.color("green3")
                    cuerpo.append(cuadro)

        time.sleep(POSPONER)

    #Funcion para ejecutar la ventana
    ventana.mainloop()

informacion()
juego()