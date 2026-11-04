#!/usr/bin/env python3

"""
practica07_nombre_equipo.py

Pedir el nombre de un equipo, como «pc-aula-07», y mostrar cuántos dígitos y
cuántos guiones contiene.
"""
digitos = 0
guiones = 0
letras = 0

nombre = input("Dime el nombe de un equipo: ")

for item in nombre:
    if item.isdigit():
        digitos = digitos + 1
    elif item == "-":
        guiones += 1 # guiones = guiones + 1
    elif item.islower() or item.isupper():
        letras += 1

print(f"Dígitos: {digitos}")
print(f"Guiones: {guiones}")
print(f"Letras: {letras}")