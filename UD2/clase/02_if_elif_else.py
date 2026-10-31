#!/usr/bin/env python3
"""
Clasificar un código de respuesta HTTP.

Pide el código que devuelve el servidor web y dice de qué tipo es.
Usaremos IF anidados.
"""
import sys
#--- Datos de entrada ---
#codigo = int(input("Código de respuesta HTTP: "))
codigo = int(sys.argv[1])

#--- Decisión y salida ---
if codigo == 200:
    print("OK: la petición se ha atendido")
elif codigo == 404:
    print("No encontrado: la página no existe")
elif codigo >=500:
    print("Error en el servidor")
else:
    print("Código no válido")

print("Fin de la comprobación")