#!/usr/bin/env python3
"""
07_ficha_servidor.py — Ficha de un servidor a partir de datos tecleados.

Pide los datos básicos de un equipo y los muestra en forma de ficha,
con el porcentaje de disco ocupado ya calculado.
"""

# --- Datos de entrada ---
nombre = input("Nombre del equipo: ")
ip = input("Dirección IP: ")
so = input("Sistema operativo: ")
ram_gb = int(input("RAM en GB: ")) # "16" lo voy a convertir a 16
disco_total_gb = int(input("Disco total en GB: "))
disco_usado_gb = int(input("Disco usado en GB: "))

# --- Cálculos ---
porcentaje = disco_usado_gb / disco_total_gb * 100

# --- Salida ---
print()
print("=" * 44)
print(f"  FICHA DEL EQUIPO: {nombre.upper()}")
print("=" * 44)
print(f"  IP:        {ip}")
print(f"  Sistema:   {so}")
print(f"  RAM:       {ram_gb} GB")
print(f"  Disco:     {disco_usado_gb}/{disco_total_gb} GB ({porcentaje:.1f} % ocupado)")
print("=" * 44)
