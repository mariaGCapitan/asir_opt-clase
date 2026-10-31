#!/usr/bin/env python3

"""
Vamos a repetir una sentencia un número X de veces
Vamos a trabajar con un contador
"""
contador = 0 #Defino una variable contador y la pongo a 0

nombre = input("Introduce tu nombre: ")
contador = contador + 1
#contador += 1
while nombre != "María":
    nombre = input("Introduce tu nombre: ")
    contador += 1

print(f"Hola María, has tardado {contador} veces en acertar")