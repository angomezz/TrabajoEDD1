from tkinter import *
import subprocess
from tkinter.font import Font
#from main import puntaje


def ejecutar_main():
    v_principal.destroy()
    subprocess.run(["python", "main.py"])

#variable para el puntaje

v_principal = Tk()
v_principal.config(bg='pink')
v_principal.geometry('600x400+40+40')
v_principal.resizable(0, 0)
v_principal.title('Pagina Principal')

# Crear frame1
frame1 = Frame(v_principal, width=600, height=70, bg="SlateGray2")
frame1.pack(side=TOP, fill=X)

# Crear título centrado en frame1
titulo = Label(frame1, text="JUEGO  WORDLE   2.0")
titulo.config(font=Font(family="Georgia", size=16), bg="SlateGray2")
titulo.place(relx=0.5, rely=0.5, anchor=CENTER)

#crear frame2
frame2 = Frame(v_principal, width=600, height=230, bg="white")
frame2.pack(side=TOP, fill=X)

# descripcion
descripcion = Label(frame2,bg="white",width=45,font=Font(family="Verdana", size=10),
                    text='''Descripcion: es un juego de palabras que tiene como \n objetivo adivinar una palabra. \n claves:\n verde: la letra esta en el lugar correcto \n amarillo: la letra esta en otra posicion \n gris: la letra no esta''')
descripcion.place(relx=0.01, rely=0.2)

# Tutulo del puntake
titulo_puntaje = Label(frame2, text="Puntuacion total", width=15, font=("Arial", 14))
titulo_puntaje.place(relx=0.65, rely=0.2)

#puntaje total(va cambiando)
titulo_puntaje = Label(frame2, text=puntaje, width=15, font=("Arial", 14))
titulo_puntaje.place(relx=0.65, rely=0.3)

#crear frame3
frame3 = Frame(v_principal, width=600, height=230, bg="white")
frame3.pack(side=TOP, fill=X)

# crear el titulo para los niveles
titulo_level = Label(frame3, text="Niveles \n Disponibles",font=("Arial", 11))
titulo_level.place(relx=0.02, rely=0.3)

#crear los 5 botones para los niveles
bot1=Button(frame3,  text="4 letras", command=ejecutar_main,bg="#80FF00")
bot1.place(relx=0.2, rely=0.3)

bot2=Button(frame3,  text="5 letras",bg="#DCFF00")
bot2.place(relx=0.35, rely=0.3)

bot3=Button(frame3,  text="6 letras", bg="#FFD500")
bot3.place(relx=0.5, rely=0.3)

bot4=Button(frame3,  text="7 letras", bg="#FF8700")
bot4.place(relx=0.65, rely=0.3)

bot5=Button(frame3,  text="8 letras", bg = "#FF2D00")
bot5.place(relx=0.8, rely=0.3)


v_principal.mainloop()
