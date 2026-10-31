#!/usr/bin/env python3
"""
Condiciones anidadas
Vamos a comprobar el usuario y contraseña de un usuario
"""

# --- Constantes ---
USUARIO = "admin"
CLAVE = "asir-2026"


usuario_pedido = input("Usuario: ")

if usuario_pedido == USUARIO:
    clave_pedido = input("Contraseña: ")
    if clave_pedido == CLAVE:
        print("Tanto el usuario como la clave son correctos")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario incorrecto")