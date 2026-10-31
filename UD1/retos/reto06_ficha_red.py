#!/usr/bin/env python3
"""
reto06_ficha_red.py — Ficha de red de un equipo.

Pide los datos de red de un equipo y los muestra en una ficha con las
etiquetas alineadas, separada por líneas de guiones.
"""

# --- Datos de entrada ---
nombre = input("Nombre del equipo: ")
ip = input("Dirección IP: ")
mascara = input("Máscara de red: ")
puerta_enlace = input("Puerta de enlace: ")
dns = input("Servidor DNS: ")

# --- Salida ---
print()
print("-" * 40)
print(f"{'EQUIPO':<18}{nombre}")
print("-" * 40)
print(f"{'Dirección IP':<18}{ip}")
print(f"{'Máscara':<18}{mascara}")
print(f"{'Puerta de enlace':<18}{puerta_enlace}")
print(f"{'DNS':<18}{dns}")
print("-" * 40)
