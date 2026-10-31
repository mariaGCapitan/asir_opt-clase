#!/usr/bin/env python3
"""
08_argumentos.py — Pasar datos al script desde la terminal, como a cualquier comando.

Uso:
    python3 08_argumentos.py srv-web-01 192.168.1.10
"""
import sys

print("Argumentos recibidos:", sys.argv)

nombre = sys.argv[1]      # el primer argumento después del nombre del script
ip = sys.argv[2]          # el segundo
print(f"Equipo {nombre} con IP {ip}")
