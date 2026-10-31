#!/usr/bin/env python3
"""
plantilla_script.py — Plantilla para empezar cualquier script del módulo.

Qué hace este script: convierte una cantidad de GB en bytes.
Autor:  (nombre)
Fecha:  (fecha)
"""

# --- Constantes: valores que no cambian, en MAYÚSCULAS ---
GB_EN_BYTES = 1024 ** 3

# --- Datos de entrada ---
tamano_gb = float(input("Tamaño en GB: "))

# --- Cálculos ---
tamano_bytes = tamano_gb * GB_EN_BYTES

# --- Salida ---
print(f"{tamano_gb} GB son {tamano_bytes:,.0f} bytes")
