#!/usr/bin/env python3

"""
Vamos a convertir los segundos a años, meses, días...
Uso: el programa tiene como argumento los segundos totales
"""
import sys

uptime = int(sys.argv[1]) 

annos = uptime // 31536000
resto = uptime % 31536000

#Un día tiene 86400 segundos
dias = resto // 86400
resto = resto % 86400 # me da el resto

horas = resto // 3600 # una hora tiene 3600 segundos
resto = resto % 3600 

minutos = resto // 60
segundos = resto % 60

print(f"El servidor lleva {annos} años, {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos encendido")