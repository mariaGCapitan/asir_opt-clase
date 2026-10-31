nombre = input("Nombre del servidor: ")
print(f"Hola, {nombre}")

ram_texto = input("RAM en GB: " )
ram = int(ram_texto)
print(f"Necesitas el dobre de RAM: {ram * 2} GB")

#Convertir directamente al pedir
discos1 = int(input("Número de discos del servidor 1: "))
discos2 = int(input("Número de discos del servidor 2: "))
print(f"Número de discos en total: {discos1 + discos2}")