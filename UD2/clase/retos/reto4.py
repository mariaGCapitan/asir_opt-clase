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

for caracter in clave: #1234567890
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
else:
    print("Longitud: NO cumple")

