#!/usr/bin/env python3
"""
Pedir el tamaño de un archivo en MB y la velocidad de la conexión en Mbps (megabits por segundo), y mostrar cuánto tardará la descarga en minutos y segundos.
Un byte son 8 bits, así que los segundos totales son tamaño × 8 / velocidad. Con un archivo de 4700 MB, el tamaño de un DVD, y una conexión de 100 Mbps.
"""
tamanno_mb = float(input("Tamaño del archivo en MB: "))
velocidad_mbps = float(input("Velocidad de la conexión en Mbbps: "))

segundos_totales = int(tamanno_mb * 8 / velocidad_mbps)

minutos = segundos_totales // 60
segundos = segundos_totales % 60
print(f"La descarga tardará {minutos} minutos y {segundos} segundos (aprox)")