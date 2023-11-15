from tkinter import  Tk, Button, Entry, Label, messagebox, PhotoImage
from tkinter import  StringVar,Frame
from tkinter import *

import random
from tkinter.font import Font


class Wordle(Frame):
	palabras = {4:'cuatro.txt', 5:'cinco.txt', 6:'seis.txt', 7:'siete.txt', 8:'ocho.txt'}
	nLetras = 0
 
	def __init__(self, master):
		super().__init__( master)
		self.fila = 0
		self.verde = 'green3'
		self.amarillo = 'gold'
		self.gris = 'SlateGray3'
		self.texto = StringVar()
		self.texto.trace("w", lambda *args: self.limitar(self.texto))
		self.create_widgets()
		self.palabra_aleatoria()
		self.resultado = 6

	def create_widgets(self):
		self.frame_titulo = Frame(self.master, bg='white', width=400, height=100)
		self.frame_titulo.grid_propagate(0)
		self.frame_titulo.grid(column=0, row=0, sticky='snew')

		self.frame_cuadros = Frame(self.master, bg='black', width=480, height=350)
		self.frame_cuadros.grid_propagate(0)
		self.frame_cuadros.grid(column=0, row=1, sticky='snew')

		self.frame_control = Frame(self.master, bg='lavender', width=400, height=100)
		self.frame_control.grid_propagate(0)
		self.frame_control.grid(column=0, row=2, sticky='snew')

		Label(self.frame_titulo,  bg= 'white',fg='black', text= 'WORDLE', 
			font=('Arial',25,'bold')).pack(side='top')

		self.alerta = Label(self.frame_control,  bg= 'black',fg='white', text= 'Alarma', 
			font=('Arial',12))
		self.alerta.pack(side= 'left', expand=True)

		self.palabra = Entry(self.frame_control, font=('Arial',15), justify = 'center', 
			textvariable = self.texto,fg='black',highlightcolor= "purple", highlightthickness=2, width=Wordle.nLetras+2)
		self.palabra.pack(side= 'left', expand=True)

		self.enviar = Button(self.frame_control, text= 'Enviar', bg='gray50',activebackground='green2',
		 fg = 'white', font=('Arial', 12,'bold'), command=self.verificar_palabra)
		self.enviar.pack(side= 'left', expand=True)

		self.limpiar = Button(self.frame_control, text= '⌫', bg='gray50',activebackground='green2',
		 fg = 'white', font=('Arial', 12,'bold'), width=4, command= lambda:self.texto.set(''))
		self.limpiar.pack(side= 'left', expand=True)
  

	def limitar(self, texto):
		if len(texto.get()) > 0:
			texto.set(texto.get()[:Wordle.nLetras])

	def palabra_aleatoria(self):
		archivo = open(Wordle.palabras[Wordle.nLetras], 'r', encoding="utf-8")
		self.conjunto_palabras = set(archivo.read().splitlines())
		self.palabra_aleatoria = random.choice(list(self.conjunto_palabras))
 

	def verificar_palabra(self):
		global puntaje_total
		global aciertos
		global fallos
  
		palabra = self.texto.get().upper()

		#x = list(filter(lambda x: palabra in x, self.conjunto_palabras)) #[i for i in conjunto_palabras if palabra in i]
		
		if palabra in self.conjunto_palabras and len(palabra)==Wordle.nLetras:
			self.alerta['text'] = ''
			print(self.palabra_aleatoria, palabra)

			if self.fila<=6:					
				for i, letra in enumerate(palabra):
					self.cuadros = Label(self.frame_cuadros, width=9-(Wordle.nLetras) if Wordle.nLetras<8 else 2,  fg='white' ,
						bg=self.gris, text= letra, font=('Geometr706 BlkCn BT',25, 'bold'))
					self.cuadros.grid(column=i, row = self.fila , padx =5, pady =5)

					if letra == self.palabra_aleatoria[i]:
						self.cuadros['bg']= self.verde

					if letra in self.palabra_aleatoria and not letra== self.palabra_aleatoria[i]:
						self.cuadros['bg']= self.amarillo

					if letra not in self.palabra_aleatoria:
						self.cuadros['bg']= self.gris

			self.fila = self.fila + 1
			if self.fila<=6 and self.palabra_aleatoria == palabra:
				self.resultado = 1
				messagebox.showinfo('GANASTE', 'FELICIDADES')
				self.master.destroy()
				self.master.quit()
				puntaje_total += 6-self.fila
				aciertos += 1
				inicio(puntaje_total)    
				print("se retorna 1")
				
			if self.fila==6 and self.palabra_aleatoria != palabra:
				messagebox.showinfo('PERDISTE', 'INTENTALO DE NUEVO')
				self.master.destroy()
				self.master.quit()
				fallos += 1
				inicio(puntaje_total)
				print("se retorna 0")
				self.resultado = 0
		else:
			self.alerta['text'] = 'No esta en BBDD'

def juego():

	ventana = Tk()
	ventana.config(bg='black')
	#ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))
	ventana.geometry('480x440+40+40')
	ventana.resizable(0,0)
	ventana.title('Wordle')
	app = Wordle(ventana)
	app.mainloop()

	return app.resultado

def inicio(puntaje):
	resultado_juego = None

	def ejecutar_juego(letras):
		
		nonlocal resultado_juego
		global puntaje_total

		Wordle.nLetras = letras
		v_principal.destroy()
		resultado_juego = juego()
		print(resultado_juego)

		#if resultado_juego == 1:
			#puntaje_total += 1  # Aumenta el puntaje total en 1
			#print("Puntaje total:", puntaje_total)
			#inicio(puntaje_total) 


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

	# Tutulo del puntaje
	titulo_puntaje = Label(frame2, text="Puntuacion total", width=15, font=("Arial", 14))
	titulo_puntaje.place(relx=0.65, rely=0.2)

	#puntaje total(va cambiando)
	titulo_puntaje = Label(frame2, text=puntaje, width=15, font=("Arial", 14))
	titulo_puntaje.place(relx=0.65, rely=0.3)
 
	titulo_aciertos = Label(frame2, text='Aciertos', width=15, font=("Arial", 14))
	titulo_aciertos.place(relx=0.65, rely=0.5)
 
	cantidad_aciertos = Label(frame2, text=aciertos, width=15, font=("Arial", 14))
	cantidad_aciertos.place(relx=0.65, rely=0.6)
 
	titulo_fallos = Label(frame2, text='Fallos', width=15, font=("Arial", 14))
	titulo_fallos.place(relx=0.65, rely=0.8)
 
	cantidad_fallos = Label(frame2, text=fallos, width=15, font=("Arial", 14))
	cantidad_fallos.place(relx=0.65, rely=0.9)

	#crear frame3
	frame3 = Frame(v_principal, width=600, height=230, bg="white")
	frame3.pack(side=TOP, fill=X)

	# crear el titulo para los niveles
	titulo_level = Label(frame3, text="Niveles \n Disponibles",font=("Arial", 11))
	titulo_level.place(relx=0.02, rely=0.3)

	#crear los 5 botones para los niveles
	bot1=Button(frame3,  text="4 letras",bg="#80FF00", command=lambda:ejecutar_juego(4))
	bot1.place(relx=0.2, rely=0.3)

	bot2=Button(frame3,  text="5 letras",bg="#DCFF00", command=lambda:ejecutar_juego(5))
	bot2.place(relx=0.35, rely=0.3)

	bot3=Button(frame3,  text="6 letras", bg="#FFD500", command=lambda:ejecutar_juego(6))
	bot3.place(relx=0.5, rely=0.3)

	bot4=Button(frame3,  text="7 letras", bg="#FF8700", command=lambda:ejecutar_juego(7))
	bot4.place(relx=0.65, rely=0.3)

	bot5=Button(frame3,  text="8 letras", bg = "#FF2D00", command=lambda:ejecutar_juego(8))
	bot5.place(relx=0.8, rely=0.3)


	v_principal.mainloop()

aciertos = 0
fallos = 0
puntaje_total = 0
inicio(0)

