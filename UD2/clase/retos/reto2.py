#!/usr/bin/env python3

"""
Acceso a la sala de servidores

La sala de servidores tiene un lector de tarjetas. El código de tarjeta válido es "SRV-07".

- Pide el código de tarjeta.
- Si es correcto, pide la hora actual (solo la hora, un número de 0 a 23).
- Solo se puede entrar entre las 8 y las 15 (ambas incluidas).

Mensajes posibles:
 Tarjeta no válida
 Fuera de horario
 Acceso permitido a la sala de servidores
"""

CODIGO= "SRV-07" 
HORA_I = 8
HORA_F = 16

codigo_pedido = input("Introduce el código de la tarjeta:")

if codigo_pedido == CODIGO:
    hora_actual = int(input("Hora actual: "))
    if hora_actual <= HORA_I and hora_actual >= HORA_F:
        print("Acceso permitido a la sala de servidores")
    else:
        print("Fuera del horario")
else:
    print("Tarjeta no válida")