#!/usr/bin/env python3
"""
Recorremos una cadena carácter a carácter


cadena = input("Dame una cadena: ")

for c in cadena:
    print(f"{c}")

#Comprobamos si una contraseña cumple el patrón
"""
"""
c.isupper() Si es mayúsucla el carácter
c.islower() si es minúsucla
c.isdigit() si es un dígito
"""
SIMBOLOS = "!@#$%&*"

num_mayuscula = 0
num_minuscula = 0
num_digitos = 0
num_simbolos = 0

clave = input("Dame la contraseña para ver si cumple con mínimo 'un símbolo', 'una mayúscula' ' una minúscula ' y ' un dígito': ")
#Ma26$

for caracter in clave:
    if caracter.isupper():
        num_mayuscula += 1
    elif caracter.islower():
        num_minuscula +=1
    elif caracter.isdigit():
        num_digitos +=1
    elif caracter in "!@#$%&*": #Está en SIMBOLOS?
        num_simbolos +=1

if num_mayuscula > 0 and num_minuscula > 0 and num_digitos > 0 and num_simbolos > 0:
    print(f"Contraseña correcta,tienes {num_simbolos} símbolos, tienes {num_mayuscula} mayúsculas, {num_minuscula} minúsculas y {num_digitos} dígitos")
else:
    print("Contraseña incorrecta")
