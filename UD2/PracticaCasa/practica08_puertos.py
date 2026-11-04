#!/usr/bin/env python3

"""
practica08_puertos.py

Mostrar los puertos del 20 al 30, uno por línea, saltándose el 22 y el 25.
"""

for p in range(20,30):
    if p == 22 or p == 25:
        continue
    print(f"Puerto: {p}")

