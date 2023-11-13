import random


archivo = open('cuatro.txt', 'r', encoding="utf-8")
conjunto_palabras = set(archivo.read().splitlines())
palabra_aleatoria = random.choice(list(conjunto_palabras))

print(conjunto_palabras)

palabra = "AMOR"

print(palabra in conjunto_palabras)