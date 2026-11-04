#!/usr/bin/env python3

"""
practica05_actualizar.py

Un equipo puede recibir una actualización si está encendido y, además, tiene
al menos 5 GB libres o está en la red de pruebas.

Preguntar si el equipo está encendido (s/n), cuántos GB libres tiene y si está
en la red de pruebas (s/n), y mostrar «Se puede actualizar» o «No se puede
actualizar».
"""
encendido = input("¿Está encendido? (s/n): ")
libre_gb = float(input("GB libres?: "))
red_pruebas = input("Estás en la red de pruebas?: (s/n): ")

if encendido == "s" and (libre_gb>= 5 or red_pruebas == "s"):
    print("Se puede actualizar")
else:
    print("No se puede actualizar")

