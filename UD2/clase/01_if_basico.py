#!/usr/bin/env python3
"""
Primera decisión: avisar cuando el disco está casi lleno
Pide el porcentaje de ocupación de un disco y avisa si alcanza el umbral
"""

#--- Datos entrada ---
porcentaje = int(input("Porcentaje de disco ocupado:"))

#--- Decisión y salida ---

if porcentaje >= 90:
    print("AVISO: el disco está casi lleno")
    print("Hay que liberar espacio")
else:
    print("Espacio suficiente")

print("Esto está fuera del IF y del ELSE. TERMINADO!!!")