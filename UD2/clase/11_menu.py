#!/usr/bin/env python3
"""
Menú que se repite hasta que se elige salir
"""
import os
os.system("clear")

while True:

    print()
    print("============= MENÚ DE ADMINISTRACIÓN ==============")
    print("1. Estado del servidor web")
    print("2. Estado de la copia de seguridad")
    print("3. Salir")
    print()

    opcion = input("Opción: ")
    if opcion == "3":
        print("Hasta pronto")
        break
    if opcion == "1":
        #lanzo el comando que me dice si el servidor está activo
        print("Servidor web: activo")
    elif opcion == "2":
        print("Copia de segurdad: completada")
    else:
        print("Opción incorrecta")


