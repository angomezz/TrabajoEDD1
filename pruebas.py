import turtle

# Clase para representar el cuadrado
class Cuadrado:
    def __init__(self, size):
        self.size = size

    def mover(self, x, y):
        self.turtle.goto(x, y)

# Clase para el juego
class Juego:
    def __init__(self):
        self.ventana = turtle.Screen()
        self.ventana.title("Snake Game")
        self.ventana.bgcolor("blue")
        self.ventana.setup(width=500, height=500)
        self.cuadrado = Cuadrado(20)
        self.crear_cuadrado()

    def crear_cuadrado(self):
        self.cuadrado.turtle = turtle.Turtle()
        self.cuadrado.turtle.shape("square")
        self.cuadrado.turtle.shapesize(stretch_wid=self.cuadrado.size/20, stretch_len=self.cuadrado.size/20)
        self.cuadrado.turtle.penup()
        self.cuadrado.turtle.goto(0, 0)

    def iniciar(self):
        # Aquí puedes implementar la lógica del juego, movimientos, colisiones, etc.
        # Por ejemplo, puedes usar un bucle para mover el cuadrado y verificar colisiones.

        # Ejemplo de movimiento
        self.cuadrado.mover(50, 50)

        self.ventana.mainloop()

# Crear el juego y comenzar
juego = Juego()
juego.iniciar()
