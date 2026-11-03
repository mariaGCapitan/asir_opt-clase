#!/usr/bin/env python3
"""
Sentencias de salto:
- Buscar el primer puerto libre y deja de buscar
- Repartir direcciones saltándonos las reservadas
"""

for puerto in range(8000,8020):
    print(f"Probando {puerto}...")
    if puerto == 8004:
        print("Puerto libre encontrado")
        break

#Las direcciones .0, .1 y .2 está reservadas para la puerta de enlace y el DNS        
for host in range(0,8):#01234567
    if host <= 2 :
        continue
    print(f"Asignada 192.168.1.{host}")
    break
