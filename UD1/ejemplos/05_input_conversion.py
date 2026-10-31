# 05_input_conversion.py — Pedir datos por teclado.

nombre = input("Nombre del servidor: ")
print(f"Hola, {nombre}")

# input() SIEMPRE devuelve texto, aunque se escriba un número
ram_texto = input("RAM en GB: ")
print(type(ram_texto))               # <class 'str'>

# Para operar hay que convertir
ram = int(ram_texto)
print(f"El doble de RAM serían {ram * 2} GB")

# Se puede convertir directamente al pedir
discos = int(input("Número de discos: "))
capacidad = float(input("Capacidad de cada disco en TB: "))
print(f"Capacidad total: {discos * capacidad} TB")

# Al revés: de número a texto, con str()
mensaje = "Total de discos: " + str(discos)
print(mensaje)
