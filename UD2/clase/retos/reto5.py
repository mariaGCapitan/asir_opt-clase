#!/usr/bin/env python3
"""
Un menú con tres opciones: 1, mostrar el nombre del equipo (pc-aula-07); 2, mostrar su dirección IP (192.168.1.57); y 3, salir. El menú se muestra de nuevo después de cada consulta, avisa si se elige una opción que no existe y, al salir, indica cuántas consultas se han hecho.
"""
import os
os.system("clear")

contador = 0

while True:

    print()
    print("============= MENÚ DE ADMINISTRACIÓN ==============")
    print("1. mostrar el nombre del equipo")
    print("2. mostrar su dirección IP")
    print("3. Salir")
    print()

    opcion = input("Opción: ")
    contador += 1
    if opcion == "3":
        print("Hasta pronto")
        break
    if opcion == "1":
        #lanzo el comando
        print("El nombre del equipo es pc-aula-07")
    elif opcion == "2":
        print("Su dirección IP es 192.168.1.57")
    else:
        print("Opción incorrecta")

print(f"Lo has intentado {contador} veces")
