from tkinter import *
from tkinter.font import Font  # Añade esta línea para importar Font

root = Tk()

# Fuente Helvetica, tamaño 16
fuente_helvetica = Font(family="Helvetica", size=16)

# Fuente Times New Roman, tamaño 16
fuente_times = Font(family="Times New Roman", size=16)

# Fuente Courier New, tamaño 16
fuente_courier = Font(family="Courier New", size=16)

# Fuente Verdana, tamaño 16
fuente_verdana = Font(family="Verdana", size=16)

# Fuente Georgia, tamaño 16
fuente_georgia = Font(family="Georgia", size=16)

# Ejemplo de etiquetas con diferentes fuentes
Label(root, text="Helvetica", font=fuente_helvetica).pack()
Label(root, text="Times New Roman", font=fuente_times).pack()
Label(root, text="Courier New", font=fuente_courier).pack()
Label(root, text="Verdana", font=fuente_verdana).pack()
Label(root, text="Georgia", font=fuente_georgia).pack()

root.mainloop()
