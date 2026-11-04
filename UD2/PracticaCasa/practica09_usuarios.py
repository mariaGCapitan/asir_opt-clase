#!/usr/bin/env python3
"""
practica09_usuarios.py

Pedir nombres de usuario, uno por uno, hasta que se escriba «fin».

Al terminar, mostrar cuántos nombres se han introducido, sin contar «fin».
"""
contador = 0
nombre = input("Dame el nombre de usuario: ")

while nombre != "fin":
    contador += 1
    nombre = input("Dame el nombre de usuario: ")

print(f"El total de nombres introducidos es {contador}")