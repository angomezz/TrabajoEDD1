from tkinter import *
import subprocess

def ejecutar_main():
    v_principal.destroy() 
    subprocess.run(["python", "main.py"])

#variable para el puntaje
puntaje=23

v_principal = Tk()
v_principal.config(bg='pink')
v_principal.geometry('600x400')
v_principal.resizable(0, 0)
v_principal.title('Pagina Principal')

# Crear frame1
frame1 = Frame(v_principal, width=600, height=70, bg="red")
frame1.pack(side=TOP, fill=X)

# Crear título centrado en frame1
titulo = Label(frame1, text="TITULOTITULO")
titulo.place(relx=0.5, rely=0.5, anchor=CENTER)

#crear frame2
frame2 = Frame(v_principal, width=600, height=230, bg="purple")
frame2.pack(side=TOP, fill=X)

# descripcion
descripcion = Label(frame2, text="Aqui va la decripcion del juego \n con niveles y explicacion \n de los colores")
descripcion.place(relx=0.1, rely=0.3)

# Tutulo del puntake
titulo_puntaje = Label(frame2, text="Puntuacion total", width=15)
titulo_puntaje.place(relx=0.6, rely=0.2)

#puntaje total(va cambiando)
titulo_puntaje = Label(frame2, text=puntaje, width=15)
titulo_puntaje.place(relx=0.6, rely=0.3)

#crear frame3
frame3 = Frame(v_principal, width=600, height=230, bg="gold")
frame3.pack(side=TOP, fill=X)

# crear el titulo para los niveles
titulo_level = Label(frame3, text="niveles \n disponibles")
titulo_level.place(relx=0.04, rely=0.3)

#crear los 5 botones para los niveles
bot1=Button(frame3,  text="4 letras", command=ejecutar_main)
bot1.place(relx=0.2, rely=0.3)

bot2=Button(frame3,  text="5 letras")
bot2.place(relx=0.35, rely=0.3)

bot3=Button(frame3,  text="6 letras")
bot3.place(relx=0.5, rely=0.3)

bot4=Button(frame3,  text="7 letras")
bot4.place(relx=0.65, rely=0.3)

bot5=Button(frame3,  text="8 letras")
bot5.place(relx=0.8, rely=0.3)


v_principal.mainloop()
