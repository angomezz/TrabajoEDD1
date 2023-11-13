
# Importing tkinter module
from tkinter import *
import subprocess

def ejecutar_main():
    v_principal.destroy() 
    subprocess.run(["python", "main.py"])
    
v_principal = Tk()
v_principal.config(bg='pink')
v_principal.geometry('600x400')
v_principal.resizable(0,0)
v_principal.title('Pagina Principal')


# Crear frames
frame1 = Frame(v_principal, width=600, height=80, bg="red")
frame2 = Frame(v_principal, width=600, height=240, bg="green")
frame3 = Frame(v_principal, width=600, height=90, bg="blue")

frame1.pack(side = TOP, expand = True, fill = BOTH)
frame2.pack(side = TOP, expand = True, fill = BOTH)
frame3.pack(side = TOP, expand = True, fill = BOTH)

titulo=Label(frame1,text="TITULOTITULO")
titulo.config()

v_principal.mainloop()





