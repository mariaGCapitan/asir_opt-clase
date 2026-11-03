#!/usr/bin/env python3

"""
Comprobador de fortaleza de contraseñas

Una contraseña debe cumplir cinco requisitos: tener 12 caracteres o más, una mayúscula, una
minúscula, un dígito y un símbolo de !@#$%&*. Pedir una contraseña y mostrar qué requisitos
cumple y cuáles no, con la valoración final: FUERTE si cumple los cinco, MEDIA si cumple tres o
cuatro y DÉBIL si cumple menos.
"""
#Para saber la longitud de una cadena se hace con ->  len(cadena).  

clave = input("Contraseña: ")
SIMBOLOS = "!@#$%&*"

hay_mayuscula = False
hay_minuscula = False
hay_digito = False
hay_simbolo = False
contador_requisitos = 0

for caracter in clave: #parcticas aoisefjñoawisdjhfñoaiwsjhdfñaidjfhlsdfhij2.clase.py
    if caracter.isupper():
        hay_mayuscula = True
    elif caracter.islower():
        hay_minuscula = True
    elif caracter.isdigit():
        hay_digito = True
    elif caracter in SIMBOLOS:
        hay_simbolo = True

if len(clave) >= 12:
    print("Longitud: cumple")
    contador_requisitos = contador_requisitos + 1
else:
    print("Longitud: NO cumple")

if hay_mayuscula == True: #if hay_mayuscula:
    print("Mayúscula: cumple")
    contador_requisitos = contador_requisitos + 1
else:
    print("Mayúscula: NO cumple")

if hay_minuscula == True:
    print("Minúsucla: cumple")
    contador_requisitos = contador_requisitos + 1
else:
    print("Minúsucla: NO cumple")

if hay_digito:
    print("Dígito: cumple")
    contador_requisitos = contador_requisitos + 1
else:
    print("Dígito: NO cumple")

if hay_simbolo:
    print("Símbolo: cumple")
    contador_requisitos = contador_requisitos + 1
else:
    print("Símbolo: NO cumple")

#print(f"El número de requisitos que cumple es: {contador_requisitos}")
if contador_requisitos == 5:
    print("Valoración: FUERTE")
elif contador_requisitos == 3 or contador_requisitos == 4:
    print("Valoración: MEDIA")
else:
    print("Valoración: DÉBIL")