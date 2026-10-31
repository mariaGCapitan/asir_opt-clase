#!/usr/bin/env python3
"""
reto07_argumentos.py — Conversor de bytes que recibe el dato desde la terminal.

Uso:
    python3 reto07_argumentos.py 734003200
"""
import sys

bytes_total = int(sys.argv[1])

kb = bytes_total / 1024
mb = kb / 1024
gb = mb / 1024

print(f"{bytes_total:,} bytes = {kb:,.2f} KB = {mb:,.2f} MB = {gb:,.2f} GB")
