import turtle
import time

# Inicializar Turtle
mi_turtle = turtle.Turtle()
mi_turtle.shape("turtle")

# Función para ocultar la turtle
def ocultar_turtle():
    mi_turtle.hideturtle()

# Función para mostrar la turtle
def mostrar_turtle():
    mi_turtle.showturtle()

# Ejemplo de uso
for i in range(5):
    # Mover la turtle y mostrarla
    mi_turtle.forward(50)
    mostrar_turtle()

    # Esperar un momento
    time.sleep(1)

    # Ocultar la turtle
    ocultar_turtle()

# Mantener la ventana abierta
turtle.done()
