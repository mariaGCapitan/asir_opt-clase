#!/usr/bin/env python3
"""
Suma el tamaño de una serie de archivos. Con el 0 indicamos que no hay más archivos
"""

total_mb = 0 #Acumulador
num_archivos = 0 #Contador

tamanno_mb = int(input("Tamaño del archivo en MB (0 para terminar): "))

while tamanno_mb != 0:
    total_mb = total_mb + tamanno_mb
    tamanno_mb = int(input("Tamaño del archivo en MB (0 para terminar): "))
    num_archivos+=1

#Fuera del while, ya ha puesto 0 el usuario
print(f"El tamaño de los archivos es: {total_mb}")
print(f"En total has pasado el tamaño de {num_archivos} archivos")