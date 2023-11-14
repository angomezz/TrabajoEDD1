from wordle import Wordle

from tkinter import  Tk, Button, Entry, Label, messagebox, PhotoImage
from tkinter import  StringVar,Frame
import random

def juego():
    ventana = Tk()
    ventana.config(bg='black')
    ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))
    ventana.geometry('480x440+40+40')
    ventana.resizable(0,0)
    ventana.title('Wordle')
    app = Wordle(ventana)
    app.mainloop()
    r = app.verificar_palabra()
    print(r)
    
juego()