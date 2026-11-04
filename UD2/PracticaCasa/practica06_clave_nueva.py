#!/usr/bin/env python3

"""
practica06_clave_nueva.py

Pedir una contraseña nueva y repetir la pregunta mientras tenga menos de 8
caracteres. Al aceptarla, mostrar «Contraseña aceptada con N caracteres».
"""

clave = input("Contraseña nueva: ")

while len(clave) < 8:
    # if clave == "pesao":
    #     print("Perdoooooona")
    #     break
    print("Demasiado corta, mínimo 8 de tamaño")
    clave = input("Contraseña nueva: ")

tamanno = len(clave)
print(f"El tamaño de la contraseña buena es {tamanno}")