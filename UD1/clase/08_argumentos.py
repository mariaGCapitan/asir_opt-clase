#!/usr/bin/env python3
"""
Vamos a pasar datos al script desde la terminal, como un comando del sistema.

Uso: ./08_argumentos.py servidor01 192.168.1.10
"""
import sys #No puedo usar los comandos de argumentos sin esto. Me hace una carga de lo que tiene 'sys'

print("Argumentos recibidos por mi script:", sys.argv)

nombrePrograma = sys.argv[0]
nombreServidor = sys.argv[1]
ip = sys.argv[2]
print(f"El programa se llama {nombrePrograma}")
print(f"Servidor {nombreServidor} con IP {ip}")

