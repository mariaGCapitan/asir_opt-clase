#!/usr/bin/env python3

"""
practica10_comprobaciones.py

Se comprueba un servicio 5 veces seguidas. En cada comprobación se pregunta si el servicio responde (s/n).

Si en alguna se responde «n», dejar de preguntar y mostrar «Fallo en la
comprobación N», con el número de la comprobación. Si las 5 son «s», mostrar
«Todo correcto».
"""
fallo = False

for comprobacion in range(1,6):
    responde = input("¿Responde el servicio?: (s/n)")
    if responde == "n":
        print(f"Fallo en la comprobación Nº {comprobacion}")
        fallo = True
        break

if fallo == False:
    print("Todo correcto")

# if comprobacion == 5:
#     print("Todo correcto")